from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Category
# Create your views here.

def index(request):
    return HttpResponse("Hello World!")


def templates_example(request):
    data = {'Name':'Divyesh Sharma'}
    return render(request,"index.html", context=data)

def category_list(request):
    categories = Category.objects.all()
    data = {'Category':categories}

    return render(request, "categories.html", context=data) 

def contactus(request):
    return HttpResponse("Welcome to abc firm!!")