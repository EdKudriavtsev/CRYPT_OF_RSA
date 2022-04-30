from __future__ import annotations

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.templatetags.static import static


class UserAvatar(models.Model):
    DEFAULT_AVATAR_PATH = 'imgs/profile_default_avatar.png'

    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars')

    @staticmethod
    def get_default_avatar_path():
        return UserAvatar.DEFAULT_AVATAR_PATH

    def __str__(self):
        return self.image.url
