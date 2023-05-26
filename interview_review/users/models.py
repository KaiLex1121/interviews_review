from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    image = models.ImageField(verbose_name='Profile picture', upload_to='profile_pictures', null=True, blank=True)
