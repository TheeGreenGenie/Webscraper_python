from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('scrape/', views.scrape_website, name='scrape_website'),
    path('download-image/<int:image_id>/', views.download_image, name='download_image'),
    path('download-all-images/<int:website_id>/', views.download_all_images, name='download_all_images'),
]
