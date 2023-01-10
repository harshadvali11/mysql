from django.db import models

# Create your models here.

class School(models.Model):
    name=models.CharField(max_length=100)
    principal=models.CharField(max_length=100)

class Student(models.Model):
    school=models.ForeignKey(School,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    age=models.IntegerField()