from django.shortcuts import render
from .models import Category, Image
# Create your views here.

def index(request):
    categories= Category.objects.all()
    images= Image.objects.all()
    ctx= {
            'categories':categories,
            'images':images,
            'title': 'Image Gallery',
        }
    
    return render(request,'index.html',ctx)


def add_category(request):
    pass


def add_image(request):
    pass

    
