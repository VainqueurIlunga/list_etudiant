from django.core import validators
from django import forms
from .models import *

class studentRegistration(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['nom','postnom','prenom','promo']
        widgets = {
            'nom': forms.TextInput(attrs={'class':'form-control'}),
            'postnom': forms.TextInput(attrs={'class':'form-control'}),
            'prenom': forms.TextInput(attrs={'class':'form-control'}),
            'promotion': forms.TextInput(attrs={'class':'form-control'}),
        }
    