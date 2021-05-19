from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello World!")


def templates_example(request):
    data = {'Name':'Divyesh Sharma'}
    return render(request,"index.html", context=data)

def contactus(request):
    return HttpResponse("Welcome to abc firm!!")