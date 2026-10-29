from django.db import models
from django.forms.fields import CharField


# Create your models here.
#bus booking details
class Bookings(models.Model):
    name=models.CharField(max_length=100)
    phone=models.IntegerField()
    email=models.EmailField()
    city=models.CharField(max_length=100,default="coimbatore")
    destination=models.CharField(max_length=100)
    passengers=models.IntegerField()
    booking_date=models.DateField()
    booking_time=models.TimeField()

#to view the available buses
class Buses_available(models.Model):
    name=models.CharField(max_length=100)
    departure=models.CharField(max_length=100)
    destinations=models.CharField(max_length=100,default="chennai",null=True)
    price=models.IntegerField()
    avail_time=models.TimeField()
    avail_date=models.DateField()

#login db for user's
class User(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

class Createuser(models.Model):
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    phone=models.IntegerField()


