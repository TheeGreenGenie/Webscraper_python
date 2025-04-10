from django.db import models

class ScrapedWebsite(models.Model):
    url = models.URLField(max_length=500)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    scraped_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url

class ScrapedImage(models.Model):
    website = models.ForeignKey(ScrapedWebsite, on_delete=models.CASCADE, related_name='images')
    image_url = models.URLField(max_length=500)
    alt_text = models.CharField(max_length=500, blank=True, null=True)
    filename = models.CharField(max_length=255, blank=True, null=True)
    image_data = models.BinaryField(blank=True, null=True)

    def __str__(self):
        return self.image_url