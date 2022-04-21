from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=70)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=70)
    
    
class PatientDetails(models.Model):
    name = models.CharField(max_length=70)
    Email = models.EmailField(max_length=100)
    DateTime = models.CharField(max_length=70)
    RoomTemp = models.CharField(max_length=50,default="00.00")
    Humidity = models.CharField(max_length=50,default="00.00")
    BodyTemp = models.CharField(max_length=50,default="00.00")

class CustomerDetails(models.Model):
    name = models.CharField(max_length=70)
    Email = models.EmailField(max_length=100)
    DateTime = models.CharField(max_length=70)
    Order = models.CharField(max_length=10000)
        