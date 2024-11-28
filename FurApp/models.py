from django.db import models

# Create your models here.
class contactdb(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.CharField(max_length=100,null=True,blank=True)
    Number = models.IntegerField(null=True,blank=True)
    Message = models.CharField(max_length=100,null=True,blank=True)
class signupdb(models.Model):
    Name_up = models.CharField(max_length=100, null=True, blank=True)
    Email_up = models.CharField(max_length=100, null=True, blank=True)
    Number_up = models.IntegerField(null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)
    Confirm = models.CharField(max_length=100, null=True, blank=True)
class cartdb(models.Model):
    Name_up = models.CharField(max_length=100, null=True, blank=True)
    Product_Name = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Total_Price = models.IntegerField(null=True,blank=True)
    cart_item=models.IntegerField(null=True,blank=True)

class orderdb(models.Model):
    Name =models.CharField(max_length=100, null=True, blank=True)
    Place =models.CharField(max_length=100, null=True, blank=True)
    Email =models.CharField(max_length=100, null=True, blank=True)
    Address =models.CharField(max_length=100, null=True, blank=True)
    Phone_Number =models.IntegerField(null=True,blank=True)
    Message =models.CharField(max_length=100, null=True, blank=True)
    Total_Price =models.IntegerField(null=True,blank=True)

