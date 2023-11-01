from django.db import models

# Create your models here.

class datas(models.Model):
    name=models.CharField(max_length=20,default="")
    age=models.IntegerField(default="")
    address=models.CharField(max_length=20,default="")
    contact=models.IntegerField(default="")
    email=models.CharField(max_length=20,default="")
