from django.db import models

# Create your models here.

class book(models.Model):
    name=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    publish=models.CharField(max_length=30)
