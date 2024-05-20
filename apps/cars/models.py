from datetime import datetime

from django.core import validators as V
from django.db import models

from rest_framework.exceptions import ValidationError

from core.models import BaseModel

from apps.auto_parks.models import AutoParksModel
from apps.cars.choices import CarChoices
from apps.cars.managers import CarManager
from core.services.upload_car_img import upload_car_img


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
        ordering = ('-id',)

    brand = models.CharField(max_length=50,
                             validators=[V.RegexValidator(regex='^(?!.*\s)[A-Z][a-z]{1,49}(?<!\s)$', message=[
                                 'First letter of brand must be only uppercase letters.',
                                 'Not aloud spaces at the beginning or end of the brand.',
                                 'Second letter of brand must be only lowercase letters.',
                                 'Length of brand must be between 3 and 50 characters.',
                             ])])
    seats = models.IntegerField(validators=[V.MinValueValidator(2), V.MaxValueValidator(10)])
    year = models.IntegerField(validators=[V.MinValueValidator(1900), V.MaxValueValidator(datetime.now().year)])
    price = models.IntegerField(validators=[V.MinValueValidator(1), V.MaxValueValidator(1000_000)])
    body_type = models.CharField(max_length=50, choices=[*CarChoices.choices])
    capacity = models.FloatField(validators=[V.MinValueValidator(0.4), V.MaxValueValidator(5)])
    image = models.ImageField(upload_to=upload_car_img, blank=True, validators=[
        V.FileExtensionValidator(['png', 'jpg', 'jpeg'])
    ])
    auto_park = models.ForeignKey(AutoParksModel, on_delete=models.CASCADE, related_name='cars')

    objects = CarManager()
