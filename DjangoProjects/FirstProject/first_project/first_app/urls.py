from django.contrib import admin
from django.urls.conf import path
from first_app import views

urlpatterns = [
    path('',views.index),
    path('contactus', views.contactus),
    path('templates_example',views.templates_example),
    path('models_example',views.category_list)

]
