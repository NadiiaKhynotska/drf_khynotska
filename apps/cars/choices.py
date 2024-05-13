from django.db.models import TextChoices


class CarChoices(TextChoices):
    SEDAN = 'SEDAN'
    HATCHBACK = 'HATCHBACK'
    SUV = 'SUV'
    COUPE = 'COUPE'
    CONVERTIBLE = 'CONVERTIBLE'
    WAGON = 'WAGON'
    VAN = 'VAN'
    TRUCK = 'TRUCK'
    PICKUP = 'PICKUP'
    ELECTRIC = 'ELECTRIC'
    HYBRID = 'HYBRID'
