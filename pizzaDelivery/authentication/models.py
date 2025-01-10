from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

from PizzaDelivery.authentication.managers import CustomUserManager


class User(AbstractUser):
    username = models.CharField(
        max_length=30,
        unique=True,
    )

    email = models.EmailField(
        max_length=80,
        unique=True,
    )

    phone_number = PhoneNumberField(
        null=False,
        unique=True,
    )

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username', 'phone_number']

    objects = CustomUserManager()

    # objects = CustomUserManager()

    def __str__(self):
        return f'<User {self.email}'

