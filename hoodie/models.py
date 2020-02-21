from django.db import models

from django.utils import timezone

from django.contrib.auth.models import User

from pyuploadcare.dj.models import ImageField

class Post(models.Model):
    photo = ImageField(blank=True, manual_crop="")
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    date_posted = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.name
    