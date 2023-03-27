from django.db import models


# Create your models here.
class imagedetails(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class friends(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    place = models.CharField(max_length=150)
    def __str__(self):
        return self.name
class farmers(models.Model):
    image = models.ImageField(upload_to='image')
    name = models.CharField(max_length=150)
    Designation = models.CharField(max_length=150)
    def __str__(self):
        return self.name
class articles(models.Model):
    image = models.ImageField(upload_to='image1')
    description = models.CharField(max_length=300)
    date = models.DateField()
