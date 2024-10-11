from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def portfolio(request):
    return HttpResponse("Hello Nacky!")

def index(request):
    template = loader.get_template('home/home.html')
    return HttpResponse(template.render({}, request))