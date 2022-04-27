from django.db import models
from django.forms import CharField, EmailField, IntegerField

# Create your models here.

class Admin_Details(models.Model):
    Admin_name = models.CharField(max_length=15)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=20)


class Book_Details(models.Model):
    Book_name = models.CharField(max_length=100)
    Authors = models.CharField(max_length=100)
    Book_code = models.IntegerField()