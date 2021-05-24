from django.db import models
from django.utils import deconstruct

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.category_name

    
class Blog(models.Model):
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=200,unique=True)
    blog_text = models.TextField()

    def __str__(self):
        return self.title

class ContactUs(models.Model):
    name = models.CharField(max_length=200,unique=False)
    email=models.EmailField(max_length=200,unique=False)
    description = models.TextField()






'''

1) Creating schema in database?
2) Performing migrations
3) Adding it in the admin.
4) Fill in some dummy data in it, via admin panel.
5) Get the data from database and display in the UI via template.

'''