from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    mobile = models.CharField(max_length=15, unique=True)
    mpin = models.CharField(max_length=10)

    REQUIRED_FIELDS = ['email', 'mobile', 'mpin']
    USERNAME_FIELD = 'username'