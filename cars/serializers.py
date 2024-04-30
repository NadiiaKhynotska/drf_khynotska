from rest_framework import serializers
from .models import CarModel


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    brand = serializers.CharField(max_length=50)
    year = serializers.IntegerField()


class CarListSerializer(CarSerializer):
    pass


class CarSerializer(CarListSerializer):
    seats = serializers.IntegerField()
    body_type = serializers.CharField(max_length=50)
    capacity = serializers.FloatField()

    def create(self, validated_data):
        car = CarModel.objects.create(**validated_data)
        return car

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
