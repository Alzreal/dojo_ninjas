from django import http
from django.shortcuts import redirect, render
from .models import *

def index(request):
    context={
        'dojos':Dojo.objects.all(),
        'ninjas':Ninja.objects.all(),
    }
    return render (request, "index.html", context)

def addDojo(request):
    Dojo.objects.create(name=request.POST['name'], city=request.POST['city'], 
    state=request.POST['state'])
    return redirect ('/')

def addNinja(request):
    Ninja.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],
    dojo=Dojo.objects.get(id=request.POST['dojo']))
    return redirect ('/')