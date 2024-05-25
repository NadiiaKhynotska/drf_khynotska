
from django_filters import rest_framework as filters

from apps.cars.serializers import CarSerializer


class CarFilter(filters.FilterSet):
    fields = CarSerializer.Meta.fields
    fields = [*fields, *[f'-{field}' for field in fields]]

    year_gt = filters.NumberFilter('year', 'gt')
    year_gte = filters.NumberFilter('year', 'gte')
    year_lt = filters.NumberFilter('year', 'lt')
    year_lte = filters.NumberFilter('year', 'lte')

    price_gt = filters.NumberFilter('price', 'gt')
    price_gte = filters.NumberFilter('price', 'gte')
    price_lt = filters.NumberFilter('price', 'lte')
    price_lte = filters.NumberFilter('price', 'lte')

    seats_gt = filters.NumberFilter('seats', 'gt')
    seats_gte = filters.NumberFilter('seats', 'gte')
    seats_lt = filters.NumberFilter('seats', 'lt')
    seats_lte = filters.NumberFilter('seats', 'lte')

    capacity_gt = filters.NumberFilter('capacity', 'gt')
    capacity_gte = filters.NumberFilter('capacity', 'gte')
    capacity_lt = filters.NumberFilter('capacity', 'lte')
    capacity_lte = filters.NumberFilter('capacity', 'lte')

    brand_starts = filters.CharFilter('brand', 'istartswith')
    brand_ends = filters.CharFilter('brand', 'iendswith')
    brand_contains = filters.CharFilter('brand', 'icontains')

    body_type_starts = filters.CharFilter('body_type', 'istartswith')
    body_type_ends = filters.CharFilter('body_type', 'iendswith')
    body_type_contains = filters.CharFilter('body_type', 'icontains')

    order = filters.OrderingFilter(
        fields = ([*fields])
    )
