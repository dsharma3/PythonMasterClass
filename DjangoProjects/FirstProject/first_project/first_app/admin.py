from django.contrib import admin
from first_app.models import Category,Blog,ContactUs
# Register your models here.
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(ContactUs)