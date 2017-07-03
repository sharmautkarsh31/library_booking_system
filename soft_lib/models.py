from __future__ import unicode_literals
import datetime
from django.db import models

# Create your models here.
class Category(models.Model):
    category_title= models.CharField(max_length=255)
    def __str__(self):
        return self.category_title

class User(models.Model):
    title= models.CharField(max_length=225)
    phone= models.CharField(max_length=15)
    issued_book= models.ForeignKey('Book', on_delete=models.CASCADE, related_name='user_issued_book', null=True, blank=True)
    past_books= models.ManyToManyField('Book', related_name='user_past_books', null=True, blank=True)
    def __str__(self):
        return self.title

class Book(models.Model):
    title= models.CharField(max_length=255)
    author= models.CharField(max_length=255)
    category= models.ManyToManyField(Category)
    issued= models.BooleanField(default=False)
    issued_on= models.DateField()
    issued_till= models.DateField()
    booked_to= models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title