from django.urls import path

from apps.users.views import UserCreateView, UsersAddAutoParkView, UsersListCreateView, UsersRetrieveUpdateDestroyView, \
    UserListView

urlpatterns = [
    path('', UserCreateView.as_view(), name='users-create'),
    path('/list', UserListView.as_view(), name='users-list'),
    #     path('', UsersListCreateView.as_view(), name='users_list_create'),
    #     path('/<int:pk>', UsersRetrieveUpdateDestroyView.as_view(), name='users_retrieve_update_destroy'),
    #     path('/<int:pk>/auto_parks', UsersAddAutoParkView.as_view(), name='users_add_auto_park'),
]
