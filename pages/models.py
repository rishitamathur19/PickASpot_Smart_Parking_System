from django.db import models

# Create your models here.
class registertable(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.BigIntegerField()
    password = models.CharField(max_length=16)

class usertable(models.Model):
    Name = models.CharField(max_length=30)
    Area = models.CharField(max_length=50)
    Email = models.EmailField()
    Phone = models.BigIntegerField()
    Date = models.DateField()
    Time = models.TimeField()