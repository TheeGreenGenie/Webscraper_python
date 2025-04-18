# Generated by Django 5.2 on 2025-04-10 17:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapedWebsite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=500)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', models.TextField(blank=True, null=True)),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('scraped_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScrapedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(max_length=500)),
                ('alt_text', models.CharField(blank=True, max_length=500, null=True)),
                ('filename', models.CharField(blank=True, max_length=255, null=True)),
                ('image_data', models.BinaryField(blank=True, null=True)),
                ('website', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='scraper.scrapedwebsite')),
            ],
        ),
    ]
