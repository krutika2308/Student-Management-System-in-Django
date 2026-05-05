from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class itpStudent(models.Model):
    name= models.CharField(max_length=100)
    age=models.IntegerField(null=True,blank=True)
    description=models.TextField()
    Image = models.ImageField(upload_to='images/', default='default.png', blank=True)


class Student(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)


    