from .tasks import generate_thumbnail_and_save_to_db
from rest_framework import serializers
from .models import ImageModel


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ['id', 'title', 'image_file', 'original_file', 'thumbnail_file', 'created_at']
        read_only_fields = ['id', 'original_file', 'thumbnail_file', 'created_at']

    def create(self, validated_data):
        # Save the image to the database
        image = ImageModel.objects.create(
            title=validated_data['title'],
            image_file=validated_data['image_file']
        )

        # Call the Celery task to generate the thumbnail and save the image to the database
        generate_thumbnail_and_save_to_db.delay(image.pk)

        return image
