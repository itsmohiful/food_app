from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_image',default='profile_image/default.jpg')

    def __str__(self):
        return f'{self.user.username}'

    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
