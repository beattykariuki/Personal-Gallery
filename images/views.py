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

def search_category(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"Results for: {search_term}"

        return render(request, 'all-images/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term."
        return render(request, 'all-images/search.html',{"message":message})

