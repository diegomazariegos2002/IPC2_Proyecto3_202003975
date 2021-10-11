from django.shortcuts import render
from django.http import HttpResponse #Change 1

# Create your views here.
def hello(request): #My function
    return HttpResponse("Hello, Django!")