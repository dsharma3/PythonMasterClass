from django import forms
from django.core.exceptions import ValidationError
from django.forms.fields import CharField
from django.forms.widgets import EmailInput, TextInput
from django.core import validators
from first_app.models import ContactUs

class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = "__all__"
        # exclude=["description"]
        # fields=("name","email")
   


    