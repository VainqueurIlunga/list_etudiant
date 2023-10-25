from django.core import validators
from django import forms
from ..models import *

class teacherRegistration(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['name','fistname','lastname','adresse']
        widgets = {
            'nom': forms.TextInput(attrs={'class':'form-control'}),
            'postnom': forms.TextInput(attrs={'class':'form-control'}),
            'prenom': forms.TextInput(attrs={'class':'form-control'}),
            'adresse': forms.TextInput(attrs={'class':'form-control'}),
        }
    