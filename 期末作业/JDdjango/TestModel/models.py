# models.py
from django.db import models

 
class Test(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=50)
    img = models.CharField(max_length=200)
    commit = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name,self.price,self.img,self.commit

class Movie(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name