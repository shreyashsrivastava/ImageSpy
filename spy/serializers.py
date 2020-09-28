from rest_framework import serializers
from .models import UploadImageTest

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadImageTest
        fields = ('name', 'image')