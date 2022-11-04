from datetime import datetime
from django.db import models


class newsArticle(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=10000000)
    created_at = models.DateTimeField(default=datetime.now,)


class image(models.Model):
    tag = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/',)
