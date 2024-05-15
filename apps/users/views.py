from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, \
    ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.auto_parks.serializer import AutoParksSerializer
from django.contrib.auth import get_user_model
from apps.users.serializers import UserSerializer

UserModel = get_user_model()


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsAuthenticated,)


class UsersListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


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
