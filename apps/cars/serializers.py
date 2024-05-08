from rest_framework import serializers

from .models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = (
            'id', 'brand', 'year', 'price', 'body_type', 'seats', 'capacity','auto_park', 'created_at', 'updated_at')

# class CarListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CarModel
#         fields = ('id', 'brand', 'year', 'created_at', 'updated_at')
