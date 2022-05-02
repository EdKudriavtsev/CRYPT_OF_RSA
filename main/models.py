from __future__ import annotations

import datetime

from django.contrib.auth.models import User
from django.db import models


class CipherHistory(models.Model):
    str_in = models.TextField(max_length=255)
    key = models.IntegerField()
    key2 = models.IntegerField()
    result = models.TextField(max_length=511)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.datetime.now)


class KeyGenHistory(models.Model):
    private_key = models.IntegerField()
    public_key = models.IntegerField()
    module_num = models.IntegerField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.datetime.now)
