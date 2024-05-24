from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from core.enums.regex_enum import RegexEnum
from core.models import BaseModel
from django.core import validators as V

from apps.users.managers import UserManager
from core.services.upload_avatar import upload_avatar


class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Meta:
        db_table = 'auth_user'
        ordering = ('-id',)

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, validators=[V.RegexValidator(*RegexEnum.PASSWORD.value)])
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()


class ProfileModel(BaseModel):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=50, validators=[
        V.RegexValidator(*RegexEnum.NAME.value)
    ])
    surname = models.CharField(max_length=50,  validators=[
        V.RegexValidator(*RegexEnum.NAME.value)
    ])
    age = models.IntegerField(validators=[V.MinValueValidator(15), V.MaxValueValidator(130)])
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to=upload_avatar, blank=True, validators=[
        V.FileExtensionValidator(['png', 'jpg', 'jpeg'])
    ])
