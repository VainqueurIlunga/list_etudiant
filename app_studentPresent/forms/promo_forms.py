from django.core import validators
from django import forms
from ..models import *

class promoRegistration(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ['nom_pro','fil']
        widgets = {
            'nom_pro': forms.TextInput(attrs={'class':'form-control'}),
            'fil': forms.TextInput(attrs={'class':'form-control'}),
        }
    