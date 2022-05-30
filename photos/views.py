from email.mime import image
from django.shortcuts import render
from .models import Category, Image

# Create your views here.

def gallery(request):
  categories=Category.objects.all()
  photos=Image.objects.all()
  
  return render(request,'photos/gallery.html', {'categories': categories,'photos':photos})

def viewPhoto(request, pk):
  photo=Image.objects.get(id=pk)
  
  return render(request,'photos/photo.html', {'photo':photo})

