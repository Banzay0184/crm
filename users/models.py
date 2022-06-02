from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(
        verbose_name='admin',
        default=False
    )
    is_director = models.BooleanField(
        verbose_name='director',
        default=False
    )
    is_worker = models.BooleanField(
        verbose_name='worker',
        default=False
    )