from copy import deepcopy

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response

from apps.auto_parks.models import AutoParksModel
from apps.auto_parks.serializer import AutoParksSerializer
from apps.cars.serializers import CarSerializer


class AutoParkListCreateView(ListCreateAPIView):
    queryset = AutoParksModel.objects.all()
    serializer_class = AutoParksSerializer


class AutoParkAddCarView(GenericAPIView):
    queryset = AutoParksModel.objects.all()
    serializer_class = AutoParksSerializer

    def post(self, *args, **kwargs):
        auto_park = self.get_object()
        data = self.request.data
        data_for_save = deepcopy(data)
        data_for_save['auto_park'] = auto_park.pk
        serializer = CarSerializer(data=data_for_save)
        serializer.is_valid(raise_exception=True)
        serializer.save(auto_park=auto_park)
        ap_serializer = AutoParksSerializer(auto_park)
        return Response(ap_serializer.data, status.HTTP_201_CREATED)

