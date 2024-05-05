from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.exceptions import ValidationError

from apps.cars.models import CarModel


def car_filter(query: QueryDict) -> QuerySet:
    qs = CarModel.objects.all()
    for key, value in query.items():
        match key:
            case 'year_gt':
                qs = qs.filter(year__gt=value)
            case 'brand_contains':
                qs = qs.filter(brand__icontains=value)
            case _:
                raise ValidationError(f"{key} is not a valid value")

    return qs
