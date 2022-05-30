from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
   name = models.CharField(max_length=100, null=False, blank=False)
   
   def __str__(self):
        return self.name
      
class Image(models.Model):   
  
  image = models.ImageField(null=False, blank=False, upload_to='photos/')
  name = models.CharField(max_length = 30)
  description = models.TextField()
  category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)

  def __str__(self):
        return self.description