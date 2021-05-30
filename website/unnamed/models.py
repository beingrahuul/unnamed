from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as text
# Create your models here.


class UserData(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.username
