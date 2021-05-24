from django.shortcuts import render
from django.http import HttpResponse
from first_app.forms import SimpleForm,CategoryForm
from first_app.models import Category
# Create your views here.

def index(request):
    return render(request,"index.html",context={"insert_me":"Hi my name is divyesh"})

def contactus(request):
    return HttpResponse("Welcome to abc firm!!")

def forms_example(request):
    form_data = SimpleForm()

    if request.method == 'POST':
        form_data = SimpleForm(request.POST)

        if form_data.is_valid():
            print("Name:",form_data.cleaned_data["name"])

    return render(request, "simple_form.html", context={'form':form_data})

def create_category(request):
    category = CategoryForm();
    if request.method == 'POST':
        category = CategoryForm(request.POST)
        if category.is_valid():
            category_model = Category()
            category_model.category_name = category.cleaned_data['category_name']
            category_model.save()
            return HttpResponse('Saved Successfully')
    return render(request, "category_form.html", context={'form':category})

'''
today's class content
'''