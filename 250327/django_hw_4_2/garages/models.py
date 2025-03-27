from django.db import models

# Create your models here.
class Garage(models.Model):
    location = models.TextField()
    capacity = models.IntegerField()
    is_parking_available = models.BooleanField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    


