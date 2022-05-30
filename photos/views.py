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

# def search(request):
#     if "term" in request.GET and request.GET["term"]:
#         term = request.GET.get("term")
#         photos = Image.search_image(term)
#         if photos != "No images found":
#             message = "Photos of '" + term + "'"
#             return render(request, "search.html", {"images":photos,"message":message,"title":term.capitalize()})
#         else:
#             message = "No images found"
#             return render(request, "search.html", {"images":[],"message":message,"title":term.capitalize()})

def search_results(request):
  if 'search' in request.GET and request.GET["search"]:
    search_term = request.GET["search"]
    searched_image = Image.search_image(search_term)
    message = f"{search_term}"
    print (searched_image)
    print (search_term)
    return render(request, 'photos/search.html',{"message":message,"images": searched_image})
