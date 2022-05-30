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

def save_image(self):
        """
        This is the function that we will use to save the instance of this class
        """
        self.save()

def delete_image(self):
        """
        This is the function that we will use to delete the instance of this class
        """
        Image.objects.get(id = self.id).delete()

def update_image(self,val):
        """
        This is the method to update the instance
        """
        Image.objects.filter(id = self.id).update(name = val)

@classmethod
def get_image_by_id(cls,image_id):
        """
        This is the method to get a specific image
        """
        return cls.objects.get(id = image_id)

@classmethod
def get_images(cls):
        return cls.objects.all()

@classmethod
def search_image(cls,category):
        """
        This is the method to search images based on a specific category
        """
        try:   
            searched_category = Category.objects.filter(name__icontains  = category)[0]
            return cls.objects.filter(category_id = searched_category.id)
        except Exception:
            return "No images found"
    
def __str__(self):
        return self.description