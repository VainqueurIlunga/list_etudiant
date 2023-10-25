from django.core import validators
from django import forms
from ..models import *

class coursRegistration(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['title','enseignant','promo']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'enseignant': forms.TextInput(attrs={'class':'form-control'}),
            'promotion': forms.TextInput(attrs={'class':'form-control'}),
        }
