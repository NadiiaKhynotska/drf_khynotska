from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from core.pagination import PagePagination

from apps.cars.filters import CarFilter
from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer, CarAddImageSerializer


class CarListView(ListAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    filter_class = CarFilter


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


class CarAddImageView(UpdateAPIView, ):
    queryset = CarModel.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CarAddImageSerializer
    http_method_names = ('put',)

    def perform_update(self, serializer):
        car: CarModel = self.get_object()
        car.image.delete()
        super().perform_update(serializer)
