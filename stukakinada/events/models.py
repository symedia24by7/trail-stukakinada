from datetime import datetime
from django.db import models

# Create your models here.
class event(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=10000000)
    hasImage = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now,)


class eventImage(models.Model):
    tag = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/',)
