from django.core import validators
from django import forms
from ..models import *

class fillierRegistration(forms.ModelForm):
    class Meta:
        model = Filliere
        fields = ['nom_fil','fac']
        widgets = {
            'nom_fil': forms.TextInput(attrs={'class':'form-control'}),
            'fac': forms.TextInput(attrs={'class':'form-control'}),
        }
    