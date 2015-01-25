from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    """Model for storing user's avatar

    :attribute user: :class: `User` object
    :attribute avatar: image uploaded by the :class: `User`
    """
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='users/', default='users/0.jpg')
