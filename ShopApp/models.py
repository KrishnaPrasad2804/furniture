from django.db import models

# Create your models here.
class categorydb(models.Model):
    Name =models.CharField(max_length=100,null=True,blank=True)
    Image = models.ImageField(upload_to="category_img",null=True, blank=True)
    Description = models.TextField(max_length=100, null=True, blank=True)
class productdb(models.Model):
    Product_Category = models.CharField(max_length=100,null=True,blank=True)
    Product_Name = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    MRP = models.IntegerField(null=True, blank=True)
    Description = models.TextField(max_length=100, null=True, blank=True)
    Country_Of_Orgin = models.CharField(max_length=100, null=True, blank=True)
    Manufactured_By = models.CharField(max_length=100, null=True, blank=True)
    Image1 = models.ImageField(upload_to="proimg",null=True,blank=True)
    Image2 = models.ImageField(upload_to="proimg", null=True, blank=True)
    Image3 = models.ImageField(upload_to="proimg", null=True, blank=True)