from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from apps.auth.views import ActivateUserView, RecoveryRequestView, RecoveryPasswordView, SocketView
urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='auth_login'),
    path('/refresh', TokenRefreshView.as_view(), name='auth_refresh'),
    path('/activate/<str:token>', ActivateUserView.as_view(), name='auth_activate'),
    path('/recover', RecoveryRequestView.as_view(), name='auth_recover_request'),
    path('/recover/<str:token>', RecoveryPasswordView.as_view(), name='auth_recovery_password'),
    path('/socket', SocketView.as_view(), name='auth_socket'),
]