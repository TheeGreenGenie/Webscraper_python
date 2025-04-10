import os
import re
import requests
from urllib.parse import urljoin, urlparse
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from bs4 import BeautifulSoup
from .models import ScrapedWebsite, ScrapedImage
import base64
import mimetypes

def index(request):
    """Home page with form to input URL for scraping"""
    return render(request, 'scraper/index.html')

def scrape_website(request):
    """Process the URL and scrape website data"""
    if request.method == 'POST':
        url = request.POST.get('url', '').strip()
        
        # Validate URL
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
            
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            # Create BeautifulSoup object
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract metadata
            title = soup.title.string if soup.title else 'No title found'
            
            # Get metadata from meta tags
            meta_description = soup.find('meta', attrs={'name': 'description'})
            description = meta_description['content'] if meta_description else 'No description found'
            
            meta_keywords = soup.find('meta', attrs={'name': 'keywords'})
            keywords = meta_keywords['content'] if meta_keywords else 'No keywords found'
            
            meta_author = soup.find('meta', attrs={'name': 'author'})
            author = meta_author['content'] if meta_author else 'No author found'
            
            # Create or update the ScrapedWebsite record
            website, created = ScrapedWebsite.objects.get_or_create(
                url=url,
                defaults={
                    'title': title,
                    'description': description,
                    'keywords': keywords,
                    'author': author
                }
            )
            
            if not created:
                website.title = title
                website.description = description
                website.keywords = keywords
                website.author = author
                website.save()
            
            # Clear existing images for this website
            website.images.all().delete()
            
            # Extract images - limit to 50
            images = []
            img_count = 0
            
            for img in soup.find_all('img'):
                if img_count >= 50:
                    break
                    
                img_url = img.get('src')
                if not img_url:
                    continue
                
                # Make the image URL absolute
                img_url = urljoin(url, img_url)
                
                # Skip data URLs
                if img_url.startswith('data:'):
                    continue
                    
                alt_text = img.get('alt', '')
                
                # Get filename from URL
                parsed_url = urlparse(img_url)
                filename = os.path.basename(parsed_url.path)
                if not filename:
                    filename = f"image_{img_count}.jpg"
                
                try:
                    # Attempt to download the image
                    img_response = requests.get(img_url, headers=headers, timeout=5)
                    if img_response.status_code == 200:
                        # Check if it's actually an image
                        content_type = img_response.headers.get('Content-Type', '')
                        if not content_type.startswith('image/'):
                            continue
                            
                        # Store image information
                        image = ScrapedImage.objects.create(
                            website=website,
                            image_url=img_url,
                            alt_text=alt_text,
                            filename=filename,
                            image_data=img_response.content
                        )
                        
                        # Create base64 data for preview
                        img_data = base64.b64encode(img_response.content).decode('utf-8')
                        img_count += 1
                        
                        images.append({
                            'id': image.id,
                            'url': img_url,
                            'alt_text': alt_text,
                            'filename': filename,
                            'data': f"data:{content_type};base64,{img_data}"
                        })
                except Exception as e:
                    continue
            
            # Prepare context for rendering
            context = {
                'website': {
                    'id': website.id, 
                    'url': url,
                    'title': title,
                    'description': description,
                    'keywords': keywords,
                    'author': author
                },
                'images': images,
                'image_count': img_count
            }
            
            return render(request, 'scraper/results.html', context)
            
        except requests.exceptions.RequestException as e:
            return render(request, 'scraper/index.html', {
                'error': f"Error accessing the website: {str(e)}"
            })
    
    return redirect('index')

def download_image(request, image_id):
    """Allow downloading of a scraped image"""
    try:
        image = ScrapedImage.objects.get(id=image_id)
        
        if not image.image_data:
            return HttpResponse("Image data not available", status=404)
            
        # Try to determine content type
        content_type = mimetypes.guess_type(image.filename)[0]
        if not content_type:
            content_type = 'application/octet-stream'
            
        response = HttpResponse(image.image_data, content_type=content_type)
        response['Content-Disposition'] = f'attachment; filename="{image.filename}"'
        return response
        
    except ScrapedImage.DoesNotExist:
        return HttpResponse("Image not found", status=404)

def download_all_images(request, website_id):
    """Create a zip of all images for download"""
    import zipfile
    import io
    
    try:
        website = ScrapedWebsite.objects.get(id=website_id)
        images = website.images.all()
        
        if not images:
            return HttpResponse("No images to download", status=404)
            
        # Create a zip file in memory
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for image in images:
                if image.image_data:
                    zip_file.writestr(image.filename, image.image_data)
        
        # Return the zip file for download
        response = HttpResponse(zip_buffer.getvalue(), content_type='application/zip')
        response['Content-Disposition'] = f'attachment; filename="{website.title}_images.zip"'
        return response
        
    except ScrapedWebsite.DoesNotExist:
        return HttpResponse("Website not found", status=404)