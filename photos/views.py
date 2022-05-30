from email.mime import image
from unicodedata import category
from django.shortcuts import render
from .models import Category, Image

# Create your views here.

def gallery(request):
  category=request.GET.get('category')
  if category==None:
    photos=Image.objects.all()
    
  else:
    photos=Image.objects.filter(category__name=category)
  
  categories=Category.objects.all()
  return render(request,'photos/gallery.html', {'categories': categories,'photos':photos})


def viewPhoto(request, pk):
  photo=Image.objects.get(id=pk)
  
  return render(request,'photos/photo.html', {'photo':photo})

