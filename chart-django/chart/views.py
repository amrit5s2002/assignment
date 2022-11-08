from django.shortcuts import render
from .models import *

# Create your views here.

def hello(request,*args, **kwargs):
    queryset = Sample.objects.all()
    return render(request,'hello.html',{'obj' : queryset})