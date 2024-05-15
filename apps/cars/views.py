from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from core.pagination import PagePagination

from apps.cars.filters import CarFilter
from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


class CarListView(ListAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    filter_class = CarFilter

    # def get_queryset(self):
    #     return car_filter(self.request.query_params.dict())


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    # car = CarModel.objects.get_specific_car()