from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Location,Category,Image

# Create your views here.
def welcome(request): 
    locations=Location.objects.all()
    categorys=Category.objects.all()
    images=Image.retrieve_all()
    return render (request, 'welcome.html',{'locations':locations,'categorys':categorys,'images':images})

def app_location(request):
    locations=Location.objects.all()
    return render (request,'welcome.html')

def app_category(request):
    categorys=Category.objects.all()
    return render (request,'welcome.html')

