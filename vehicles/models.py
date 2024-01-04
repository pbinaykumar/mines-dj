from django.db import models

# Create your models here.

class Vehicle(models.Model):
    vehicle_tag_id = models.CharField(max_length=21,primary_key=True)
    vehicle_number = models.CharField(max_length=21)
    vehicle_name = models.CharField(max_length=51)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class VehicleStatus(models.Model):
    STATUS = (
        ('1','Talcher Mines'),
        ('2','Jharkhand Mines'),
        ('3','Parked'),
        ('4','Weighted'),
        ('5','Dumped'),
    )
    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    status = models.CharField(max_length=21, choices=STATUS)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)