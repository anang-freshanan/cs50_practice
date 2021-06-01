from django.db import models

# Create your models here.
class Taxistand(models.Model):
    code = models.CharField(max_length=3)
    location = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"
        
class Taxi(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    rate = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"