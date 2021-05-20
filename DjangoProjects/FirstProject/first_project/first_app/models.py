from django.db import models
from django.db.models import deletion

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=264, unique= True)

    def __str__(self):
        return self.category_name

class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=264, unique=True)
    blog_text = models.TextField()

    def __str__(self):
        return self.title