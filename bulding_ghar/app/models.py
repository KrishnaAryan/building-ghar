from django.db import models

# Create your models here.
class Baner(models.Model):
    image=models.ImageField(upload_to='images/baner')