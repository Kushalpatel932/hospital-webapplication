from distutils.command.upload import upload
from pyexpat import model
from unicodedata import name
from django.db import models

# Create your models here.
class appointment(models.Model):
    name=models.CharField(max_length=50)
    email= models.EmailField()
    phone =models.IntegerField()
    date  = models.DateField()
    department = models.CharField(max_length=50)
    doctor = models.CharField(max_length=50)
    message = models.TextField()
    
    def __str__(self):
        return self.name

class doctors(models.Model):
    drname = models.CharField(max_length=50)
    drpost= models.CharField(max_length=50)
    drabout = models.TextField()
    drimage=models.ImageField(upload_to='drimage')
    def __str__(self):
        return self.drname
class feedback(models.Model):
    uname = models.CharField(max_length=50)
    upost = models.CharField(max_length=50)
    ufeedback = models.TextField()
    uimage = models.ImageField(upload_to='userimage')
    #u --> user 
    def __str__(self):
        return self.uname
