from django.urls import path,re_path
from . import views



urlpatterns = [
  path('', views.gallery, name='gallery'),
  path('photo/<str:pk>/', views.viewPhoto, name='photo'),
  re_path(r"^search/",views.search_results, name = "search"),
]