from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class AddressModel(models.Model):
    city = models.CharField(max_length = 20)
    zipcode = models.CharField(max_length = 20)

class UserModel(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # address = models.ForeignKey(AddressModel, on_delete=models.PROTECT)

class Cat(models.Model):
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    name = models.TextField()

class Restaurant(models.Model):
    name = models.CharField(max_length=1024)
    phone = PhoneNumberField(blank=True)
