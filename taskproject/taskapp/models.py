from django.db import models

#from taskapp.forms import mobile_num
from django.core import validators

# Create your models here.
class organization(models.Model):
    cname=models.CharField(max_length=64)
    cemployees=models.IntegerField()
    cid=models.IntegerField()
    caddr=models.CharField(max_length=64)
    cedate=models.DateField()

class department(models.Model):
    STATUS_CHOICE=(("development","Development"),("automation","Automation"),
                   ("testing","Testing"),("supporting","Supporting"),("admin","Admin"))
    department=models.CharField(max_length=64,choices=STATUS_CHOICE)


class designation(models.Model):
    STATUS_CHOICE = (("associate", "Associate"), ("softwareengineer","Softywareengineer"), ("software", "Softwarese"), ("tl", "Tl"),
    ("manager", "Manager"))
    designation = models.CharField(max_length=64, choices=STATUS_CHOICE)



class employee(models.Model):
    ename=models.CharField(max_length=64)
    eno=models.IntegerField()
    esal=models.IntegerField()
    etech=models.CharField(max_length=64)
    eaddr=models.CharField(max_length=64)
    email=models.EmailField()
    emobileno=models.IntegerField()

class empac(models.Model):
    elogin=models.DateTimeField()
    elogout=models.DateTimeField()
    breakhourstart=models.DateTimeField()
    breakhourend=models.DateTimeField()


