from django.urls import path

from apps.users.views import UserBlockView, UserUnBlockView, UsersAddAutoParkView, UsersListCreateView, \
    UsersRetrieveUpdateDestroyView, UserAddAvatarView, AddEmailView

urlpatterns = [
    path('', UsersListCreateView.as_view(), name='users_list_create'),
    path('/avatars', UserAddAvatarView.as_view(), name='users_add_avatar'),
    path('/<int:pk>/block', UserBlockView.as_view(), name='users_block'),
    path('/<int:pk>/unblock', UserUnBlockView.as_view(), name='users_unblock'),
    path('/<int:pk>', UsersRetrieveUpdateDestroyView.as_view(), name='users_retrieve_update_destroy'),
    path('/<int:pk>/auto_parks', UsersAddAutoParkView.as_view(), name='users_add_auto_park'),
    path('/test', AddEmailView.as_view(), name='users_sent_email')
]
