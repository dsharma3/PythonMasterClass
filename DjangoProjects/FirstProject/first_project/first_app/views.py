from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,"index.html",context={"insert_me":"Hi my name is divyesh"})

def contactus(request):
    return HttpResponse("Welcome to abc firm!!")

