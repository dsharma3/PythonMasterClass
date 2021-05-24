from django import forms
from django.forms.widgets import EmailInput, TextInput
from django.core import validators
from django.core.exceptions import ValidationError

class SimpleForm(forms.Form):
    name = forms.CharField(widget=TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget=EmailInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    botcheck = forms.CharField(widget=forms.HiddenInput(attrs={'class':'form-control'}), required=False,validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        clean_data = super().clean()
        print('clean function called')
        name = clean_data['name']

        if name[0] !='z':
            print('validation occured')

            raise ValidationError("invalid")


class CategoryForm(forms.Form):
    category_name = forms.CharField(widget=TextInput(attrs={'class':'form-control'}),required=False,validators=[validators.MaxLengthValidator(10)])