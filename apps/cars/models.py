from django.db import models

from core.models import BaseModel

from apps.auto_parks.models import AutoParksModel


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=50)
    seats = models.IntegerField()
    year = models.IntegerField()
    price = models.IntegerField()
    body_type = models.CharField(max_length=50)
    capacity = models.FloatField()
    auto_park = models.ForeignKey(AutoParksModel, on_delete=models.CASCADE, related_name='cars')

