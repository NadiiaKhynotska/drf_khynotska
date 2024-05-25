from django.db import models


class CarManager(models.Manager):
    def get_specific_car(self, brand_name):
        car = self.filter(brand_name=brand_name)
        return car