from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from apps.auto_parks.serializer import AutoParksSerializer
from django.contrib.auth import get_user_model
from apps.users.serializers import UserSerializer
from core.premissions import IsAuthenticatedForGetOrWriteOnly

UserModel = get_user_model()


class UsersListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedForGetOrWriteOnly,)


class UserBlockView(GenericAPIView):
    # queryset = UserModel.objects.all()
    permission_classes = (IsAdminUser,)

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

    def post(self, *args, **kwargs):
        user = self.get_object()
        data = self.request.data
        serializer = AutoParksSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data, status.HTTP_201_CREATED)
