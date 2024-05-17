from django.urls import path

from apps.cars.views import CarListView, CarRetrieveUpdateDestroyView, CarAddImageView

urlpatterns = [
    path('', CarListView.as_view(), name='cars_list'),
    path('/<int:pk>/images', CarAddImageView.as_view(), name='cars_add_image'),
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view(),name='cars_retrieve_update_destroy'),
]