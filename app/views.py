from django.shortcuts import render
from django.views.generic import ListView
from app.models import *

# Create your views here.
class School_list(ListView):
    model=School  # these two steps are responsible for getting all objects and creating a dictionary 
    context_object_name='schools'
    #ordering=['Sname']
    template_name='app/School_list.html'
    #queryset=School.objects.filter(Sname='DPS')


class Student_list(ListView):
    model=Student
    context_object_name='students'
