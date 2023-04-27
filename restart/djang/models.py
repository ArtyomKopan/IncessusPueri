from django.db import models

class Post(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField
    context = models.TextField(blank=True)
    is_released = models.BooleanField(default=True)
    


# Create your models here.
