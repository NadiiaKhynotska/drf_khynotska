from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from apps.auth.serializers import EmailSerializer, PasswordSerializer
from apps.users.serializers import UserSerializer
from core.services.jwt_service import JWTService, ActivateToken, RecoverToken, SocketToken
from core.services.email_service import EmailService
from rest_framework_simplejwt.serializers import TokenRefreshSerializer

UserModel = get_user_model()


class ActivateUserView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, *args, **kwargs):
        token = kwargs['token']
        user = JWTService.check_token(token, ActivateToken)
        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RecoveryRequestView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = EmailSerializer

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(UserModel, **serializer.data)
        EmailService.recovery_email(user)
        return Response({'detail': 'Check your email to reset your password'}, status.HTTP_200_OK)


class RecoveryPasswordView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PasswordSerializer

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        token = kwargs['token']
        user = JWTService.check_token(token, RecoverToken)
        user.set_password(serializer.data['password'])
        user.save()
        return Response({'detail': 'Your password is changed'}, status.HTTP_200_OK)


class SocketView(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get_serializer(self, *args, **kwargs):
        pass

    def get(self, *args, **kwargs):
        token = JWTService.create_token(self.request.user, SocketToken)
        return Response({'token': str(token)}, status.HTTP_200_OK)


@method_decorator(name='post', decorator=swagger_auto_schema(responses={status.HTTP_200_OK: TokenRefreshSerializer()}, security=[]))
class TokenPairView(TokenObtainPairView):
    pass
