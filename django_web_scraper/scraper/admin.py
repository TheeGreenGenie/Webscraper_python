from django.contrib import admin
from .models import ScrapedWebsite, ScrapedImage

class ScrapedImageInline(admin.TabularInline):
    model = ScrapedImage
    extra = 0
    fields = ('image_url', 'alt_text', 'filename')
    readonly_fields = ('image_url', 'alt_text', 'filename')
    can_delete = False
    max_num = 0
    
    def has_add_permission(self, request, obj=None):
        return False

@admin.register(ScrapedWebsite)
class ScrapedWebsiteAdmin(admin.ModelAdmin):
    list_display = ('url', 'title', 'scraped_at')
    search_fields = ('url', 'title', 'description')
    readonly_fields = ('url', 'title', 'description', 'keywords', 'author', 'scraped_at')
    inlines = [ScrapedImageInline]
    
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False

@admin.register(ScrapedImage)
class ScrapedImageAdmin(admin.ModelAdmin):
    list_display = ('image_url', 'website', 'filename')
    search_fields = ('image_url', 'filename', 'alt_text')
    readonly_fields = ('website', 'image_url', 'alt_text', 'filename')
    
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False