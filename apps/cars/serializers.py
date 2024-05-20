from rest_framework import serializers
from django.core.files import File

from .models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = (
            'id', 'brand', 'year', 'price', 'body_type', 'seats', 'capacity', 'auto_park', 'image', 'created_at',
            'updated_at')

    def validate(self, attrs):
        year = attrs['year']
        price = attrs['price']
        if year == price:
            raise serializers.ValidationError({'details': f'year - {year} must not be the same as price - {price}'})
        return attrs


class CarAddImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('image',)
        extra_kwargs = {'image': {'required': True}}

    def validate_image(self, image: File):
        max_size = 100 * 1024
        if image.size > max_size:
            raise serializers.ValidationError(f'Max size is 100Kb')
        return image
