from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello world from the home page")
    return render(request,'index.html')

def about(request):
    return HttpResponse("Hello world from the about page")

def contact(request):
    return HttpResponse("Hello world from the contact page")
