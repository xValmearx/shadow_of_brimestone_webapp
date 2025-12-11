from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Our custom user model"""

    date_of_birth = models.DateField(max_length=8, null=True, blank=True)

    def __str__(self):
        return self.username
