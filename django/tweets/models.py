from __future__ import unicode_literals

from django.db import models


class Tweet(models.Model):
    """Model for Tweet."""

    id = models.BigIntegerField(primary_key=True)
    author = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
