from django.db.models import QuerySet
from django.http import QueryDict

from rest_framework.exceptions import ValidationError

from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


def car_filter(query: QueryDict) -> QuerySet:
    qs = CarModel.objects.all()
    for key, value in query.items():
        match key:
            case 'year_gt':
                qs = qs.filter(year__gt=value)
            case 'year_gte':
                qs = qs.filter(year__gte=value)
            case 'year_lt':
                qs = qs.filter(year__lt=value)
            case 'year_lte':
                qs = qs.filter(year__lte=value)

            case 'price_gt':
                qs = qs.filter(price__gt=value)
            case 'price_gte':
                qs = qs.filter(price__gte=value)
            case 'price_lt':
                qs = qs.filter(price__lt=value)
            case 'price_lte':
                qs = qs.filter(price__lte=value)

            case 'seats_gt':
                qs = qs.filter(seats__gt=value)
            case 'seats_gte':
                qs = qs.filter(seats__gte=value)
            case 'seats_lt':
                qs = qs.filter(seats__lt=value)
            case 'seats_lte':
                qs = qs.filter(seats__lte=value)

            case 'capacity_gt':
                qs = qs.filter(capacity__gt=value)
            case 'capacity_gte':
                qs = qs.filter(capacity__gte=value)
            case 'capacity_lt':
                qs = qs.filter(capacity__lt=value)
            case 'capacity_lte':
                qs = qs.filter(capacity__lte=value)

            case 'brand_starts':
                qs = qs.filter(brand__istartswith=value)
            case 'brand_ends':
                qs = qs.filter(brand__iendswith=value)
            case 'brand_contains':
                qs = qs.filter(brand__icontains=value)

            case 'body_type_starts':
                qs = qs.filter(body_type__istartswith=value)
            case 'body_type_ends':
                qs = qs.filter(body_type__iendswith=value)
            case 'body_type_contains':
                qs = qs.filter(body_type__icontains=value)

            case 'order':
                fields = CarSerializer.Meta.fields
                fields = [*fields, *[f'-{field}' for field in fields]]
                if value not in fields:
                    raise ValidationError({'details': f'{value} not in {fields}'})

                qs = qs.order_by(value)

            case _:
                raise ValidationError(f"{key} is not a valid value")

    return qs
