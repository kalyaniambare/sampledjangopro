from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.BigIntegerField(null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
