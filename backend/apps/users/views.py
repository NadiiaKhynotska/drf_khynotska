import os

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response

from apps.auto_parks.serializer import AutoParksSerializer
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from apps.users.models import ProfileModel
from apps.users.serializers import UserSerializer, ProfileAvatarSerializer
from core.permissions import IsAuthenticatedForGetOrWriteOnly

UserModel = get_user_model()


class UsersListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class UserAddAvatarView(UpdateAPIView, ):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileAvatarSerializer
    http_method_names = ('put',)

    def get_object(self):
        return self.request.user.profile

    def perform_update(self, serializer):
        profile: ProfileModel = self.get_object()
        profile.avatar.delete()
        super().perform_update(serializer)


class UserBlockView(GenericAPIView):
    # queryset = UserModel.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = UserSerializer

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_active:
            user.is_active = False
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserUnBlockView(GenericAPIView):
    # queryset = UserModel.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_active:
            user.is_active = True
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UsersRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class UsersAddAutoParkView(GenericAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def post(self, *args, **kwargs):
        user = self.get_object()
        data = self.request.data
        serializer = AutoParksSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data, status.HTTP_201_CREATED)


class AddEmailView(GenericAPIView):
    permission_classes = (AllowAny, )

    def get_serializer(self, *args, **kwargs):
        pass

    def get(self, *args, **kwargs):
        template = get_template('test_email.html')
        html_content = template.render({'name': 'Nadiia'})
        msg = EmailMultiAlternatives('First email', from_email=os.environ.get('EMAIL_HOST'),
                                     to=['nadinyman@gmail.com'])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
        return Response(status=status.HTTP_200_OK)
