from django import http
from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("my work")
