from django import forms
from django.core.exceptions import ValidationError
from django.forms.fields import CharField
from django.forms.widgets import EmailInput, TextInput
from django.core import validators

class ContactUsForm(forms.Form):
    name = forms.CharField(widget=TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=EmailInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))


    