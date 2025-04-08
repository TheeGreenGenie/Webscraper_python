from django.shortcuts import render
from .scraper import fetch_data
from .analyzer import analyze_data

def home(request):
    return render(request, 'scraper_app/home.html')

def results(request):
    url = request.GET.get('url', 'https://example.com')
    soup = fetch_data(url)
    if soup:
        summary, details = analyze_data(soup)
    else:
        summary, details = "Failed to fetch data", {}
    context = {
        'summary': summary,
        'details': details,
    }
    return render(request, 'scraper_app/results.html', context)

def about(request):
    return render(request, 'scraper_app/about.html')
