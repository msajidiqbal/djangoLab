from django.db import models
from django.contrib.auth.models import AbstractUser
#  we can also use AbstractBaseUser as recommended by django which is base class for AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    # AbstractUser provide basic user fields
    age = models.PositiveIntegerField(null=True,blank=True)
