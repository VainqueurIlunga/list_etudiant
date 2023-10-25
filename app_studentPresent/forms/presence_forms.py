from django.core import validators
from django import forms
from ..models import *


class presenceRegistration(forms.ModelForm):
    class Meta:
        model = Participation
        fields = ['etudiant', 'cours',]
        widgets = {
            'etudiant': forms.TextInput(attrs={'class':'form-control'}),
            'cours': forms.TextInput(attrs={'class':'form-control'}),
        }
