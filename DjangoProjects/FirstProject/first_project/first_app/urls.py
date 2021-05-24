from first_app.models import Category
from django.contrib import admin
from django.urls.conf import path
from first_app import views

urlpatterns = [
    path('',views.index),
    path('contactus', views.contactus),
    path('forms_example', views.forms_example), 
    path('category',views.create_category)
]
