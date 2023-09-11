from django.db import models

# Create your models here.
class Instrument(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()