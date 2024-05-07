from django.db import models

from core.models import BaseModel


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=50)
    seats = models.IntegerField()
    year = models.IntegerField()
    price = models.IntegerField()
    body_type = models.CharField(max_length=50)
    capacity = models.FloatField()



