from django.db import models

# Create your models here.


class Student(models.Model):

    id       = models.AutoField(primary_key=True)
    name     = models.CharField(max_length=100, default='Anonymous')
    college  = models.CharField(max_length=100)
    sclass   = models.CharField(max_length=100)
    avg      = models.FloatField(default=0.0)
    m1       = models.CharField(max_length=100)
    d1       = models.FloatField()
    m2       = models.CharField(max_length=100)
    d2       = models.FloatField()
    m3       = models.CharField(max_length=100)
    d3       = models.FloatField()
    m4       = models.CharField(max_length=100)
    d4       = models.FloatField()
    m5       = models.CharField(max_length=100)
    d5       = models.FloatField()
    m6       = models.CharField(max_length=100)
    d6       = models.FloatField()
    m7       = models.CharField(max_length=100)
    d7       = models.FloatField()
