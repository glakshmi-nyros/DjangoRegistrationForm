# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
from django.http import HttpResponseRedirect


from .models import User_Details





def index(request):
	return render(request, 'basic.html')
def register(request):
    return render(request, 'register.html')


def user_register(request):
    if(request.method == 'POST'):
            email=request.POST['email_id']
            password=request.POST['password']
            uname=request.POST['user_name']
            cpassword=request.POST['confirm_password']
            phno=request.POST['contact_number']
           
            
            
            compose_query=User_Details(email_id=email,password=password,user_name=uname,
                                       confirm_password=cpassword,contact_number=phno);
            compose_query.save()
            return render(request,'register.html')
   

   # messages.add_message(request, messages.INFO, 'User registered successfully')


def result(request):
    details = User_Details.objects.order_by('id')
    template = loader.get_template('result.html')
    context = {
        'details': details,
    }
    return render(request,'result.html',context)



                
        