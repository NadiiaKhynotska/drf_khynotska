from django.urls import path
from apps.cars.views import CarListCreateView, CarRetrieveUpdateDestroyView

urlpatterns = [
    path('', CarListCreateView.as_view(), name='cars_list_create'),
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view(),name='cars_retrieve_update_destroy'),
]