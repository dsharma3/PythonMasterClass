from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Category, ContactUs
from first_app.forms import ContactUsForm
# Create your views here.

def index(request):
    return render(request,"index.html")


def templates_example(request):
    data = {'Name':'Divyesh Sharma'}
    return render(request,"index.html", context=data)

def category_list(request):
    categories = Category.objects.all()
    data = {'Category':categories}

    return render(request, "categories.html", context=data) 

def contactus(request):
    if request.method == 'POST':
        contactus = ContactUsForm(request.POST)

        print(contactus.errors)
        if contactus.is_valid():
            print("Got the data")

            print('NAME:',contactus.cleaned_data['name'])
            print('Email:',contactus.cleaned_data['email'])
            print('Description:',contactus.cleaned_data['description'])
           
            contactus.save()

        else:
            return HttpResponse('Invalid Data')
    contactus = ContactUsForm()
    forms_dictionary = {'form':contactus}
    return render(request,'contactus.html',context=forms_dictionary)