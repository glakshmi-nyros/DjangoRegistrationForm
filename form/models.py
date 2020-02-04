# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here.
class User_Details(models.Model):
    
    email_id = models.CharField(max_length=50)
    password = models.CharField(max_length=50,default='0000000')
    user_name=models.CharField(max_length=50,default='0000000')
    confirm_password=models.CharField(max_length=50,default='0000000')
    contact_number=models.CharField(max_length=50,default='0000000')

   
    def __str__(self):
        return self.user_name
        '''class mydatabase(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_id = models.EmailField()''' 