from django.db import models
from secretary.models import *
# Create your models here.


class Watchman(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20,blank=True)
    contact = models.CharField(max_length=20)
    profile_pic = models.FileField(upload_to="media\images",default="media\images\default.png")
    # Watchman Profile
    gender = models.CharField(max_length=20,blank=True)
    status = models.CharField(max_length=20,default='Pending')
    age = models.CharField(max_length=20,blank=True)
    state = models.CharField(max_length=30,blank=True)
    country = models.CharField(max_length=30,blank=True)
    city = models.CharField(max_length=30,blank=True)
    address = models.CharField(max_length=200,blank=True)
    aboutme = models.TextField(max_length=500,blank=True)
    work = models.CharField(max_length=20,blank=True)
    blood_grp = models.CharField(max_length=200,blank=True)
    birthdate = models.DateField(blank=True,null=True)
    vechicle_deatails = models.CharField(max_length=200,blank=True)
    marrial_status = models.CharField(max_length=200,blank=True)
    
    def __str__(self):
        return self.firstname
        

