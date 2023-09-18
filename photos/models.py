from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    
class Photo(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=3000)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    image_file = models.ImageField(upload_to="uploads/", null=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)