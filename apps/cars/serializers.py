from rest_framework import serializers

from .models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = (
            'id', 'brand', 'year', 'price', 'body_type', 'seats', 'capacity','auto_park', 'created_at', 'updated_at')

    def validate(self, attrs):
        year = attrs['year']
        price = attrs['price']
        if year == price:
            raise serializers.ValidationError({'details': f'year - {year} must not be the same as price - {price}'})
        return attrs