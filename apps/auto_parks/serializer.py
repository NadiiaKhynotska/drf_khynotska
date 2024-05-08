from rest_framework import serializers

from apps.auto_parks.models import AutoParksModel
from apps.cars.serializers import CarSerializer


class AutoParksSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = AutoParksModel
        fields = ('id', 'name', 'created_at', 'updated_at', 'cars')
