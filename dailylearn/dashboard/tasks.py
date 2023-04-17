from django.core.files.base import ContentFile
from celery import shared_task
from PIL import Image
from .models import ImageModel


@shared_task
def generate_thumbnail_and_save_to_db(image_id):
    # Get the image from the database
    image = ImageModel.objects.get(pk=image_id)

    # Open the image file using Pillow
    with image.image_file.open('rb') as f:
        img = Image.open(f)

        # Generate the thumbnail using Pillow
        thumbnail = img.thumbnail((100, 100))

    # Save the thumbnail to the database
    thumbnail_file = ContentFile(thumbnail.tobytes())
    image.thumbnail_file.save('thumbnail.jpg', thumbnail_file, save=True)

    # Save the original image to the database
    original_file = ContentFile(img.tobytes())
    image.original_file.save('original.jpg', original_file, save=True)