# models.py

from django.db import models


class ImageModel(models.Model):
    title = models.CharField(max_length=255)
    image_file = models.ImageField(upload_to='images/')

    # These fields will be populated by the Celery task
    original_file = models.ImageField(upload_to='images/original/')
    thumbnail_file = models.ImageField(upload_to='images/thumbnail/')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
