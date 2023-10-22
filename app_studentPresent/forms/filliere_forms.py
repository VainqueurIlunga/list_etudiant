from django.core import validators
from django import forms
from ..models import *

class fillierRegistration(forms.ModelForm):
    class Meta:
        model = Filliere
        fields = ['libelle','faculte',]
        widgets = {
            'libelle': forms.TextInput(attrs={'class':'form-control'}),
            'faculte': forms.TextInput(attrs={'class':'form-control'}),
        }
    