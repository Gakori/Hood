from django.db import models

from django.utils import timezone

from django.urls import reverse

from django.contrib.auth.models import User

from pyuploadcare.dj.models import ImageField

class Post(models.Model):
    photo = ImageField(blank=True, manual_crop="")
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'
    