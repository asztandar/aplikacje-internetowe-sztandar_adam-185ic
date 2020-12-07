from django.db import models

# Create your models here.

class Car(models.Model):
    brand = models.CharField(max_length=60)
    model = models.CharField(max_length=60)
    def __str__(self):
        return self.model