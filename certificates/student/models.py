from django.db import models

# Create your models here.

class Grades(models.Model):

    id       = models.AutoField(primary_key=True)
    sclass   = models.CharField(max_length=100)
    college  = models.CharField(max_length=100)

class Student(models.Model):

    id       = models.AutoField(primary_key=True)
    name     = models.CharField(max_length=100, default='Anonymous')
    college  = models.CharField(max_length=100)
    grades   = models.ManyToManyField(Grades)
