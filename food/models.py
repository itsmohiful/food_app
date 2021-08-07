from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class FoodItem(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    price = models.FloatField(default='00')
    image = models.ImageField(default='item_img/default.png',upload_to='item_img')
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("food-detail", kwargs={"pk": self.pk})
    