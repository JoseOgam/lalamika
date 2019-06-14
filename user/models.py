from django.db import models

from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    name = models.CharField(max_length=30, )
    regno = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

    data_register = models.DateField(auto_now_add=True, )

    def __str__(self):
        return '{name} ({regno})'.format(name=self.name, regno=self.regno, )
