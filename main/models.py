from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

GENDER_MALE = 'male'
GENDER_FEMALE = 'female'
GENDER_CHOICES = [
    (GENDER_MALE, 'male'),
    (GENDER_FEMALE, 'female'),
]


class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=200, default=None, null=True)
    display_name = models.CharField(max_length=200, default=None, null=True)
    gender = models.CharField(max_length=200, default=None, null=True, choices=GENDER_CHOICES)

    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
