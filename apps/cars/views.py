from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from apps.cars.filters import car_filter
from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer

# class CarListCreateView(GenericAPIView):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#     def get(self, *args, **kwargs):
#         # cars = CarModel.objects.filter(brand='Djeep', year=2008)
#         # qs = CarModel.objects.filter(year__range=(2008, 2017)).order_by('-year')
#         # qs = qs[1:2]
#         # qs = CarModel.objects.filter(Q(brand='Djeep') | Q(year=2018) & Q(pk=6))
#         # count = qs.count()
#         # qs = car_filter(self.request.query_params.dict())
#         qs = self.get_queryset()
#         serializer = self.get_serializer(qs, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         serializer = self.get_serializer(data=data)
#         serializer.is_valid(raise_exception=True)
#
#         # if not serializer.is_valid():
#         #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#
#         serializer.save()
#         return Response(serializer.data, status.HTTP_201_CREATED)
# class CarListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
#     serializer_class = CarSerializer
#     queryset = CarModel.objects.all()
#
#     def get(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)

class CarListView(ListAPIView):
    serializer_class = CarSerializer

    # queryset = CarModel.objects.all()

    def get_queryset(self):
        return car_filter(self.request.query_params.dict())


# class CarRetrieveUpdateDestroyView(GenericAPIView):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     def get(self, *args, **kwargs):
#         # pk = kwargs['pk']
#         # car = get_object_or_404(CarModel, pk=pk)
#         car = self.get_object()
#         serializer = self.get_serializer(car)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         # pk = kwargs['pk']
#         data = self.request.data
#         car = self.get_object()
#         serializer = self.get_serializer(car, data)
#         serializer.is_valid(raise_exception=True)
#         # try:
#         #     car = CarModel.objects.get(pk=pk)
#         # except CarModel.DoesNotExist:
#         #     raise Http404()
#         # serializer = CarSerializer(car, data)
#         # if not serializer.is_valid():
#         #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         # pk = kwargs['pk']
#         data = self.request.data
#         car = self.get_object()
#         serializer = self.get_serializer(car, data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         # try:
#         #     car = CarModel.objects.get(pk=pk)
#         # except CarModel.DoesNotExist:
#         #     raise Http404()
#         #
#         # serializer = CarSerializer(car, data, partial=True)
#         # if not serializer.is_valid():
#         #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         # pk = kwargs['pk']
#         # try:
#         #     CarModel.objects.get(pk=pk).delete()
#         # except CarModel.DoesNotExist:
#         #     raise Http404()
#         self.get_object().delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# class CarRetrieveUpdateDestroyView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     def retrieve(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
#
#     def partial_update(self, request, *args, **kwargs):
#         return super().partial_update(request, *args, **kwargs)
#
#     def update(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)
#
#     def destroy(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)
class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
