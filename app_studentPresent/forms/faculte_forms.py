from django.core import validators
from django import forms
from ..models import *

class faculteRegistration(forms.ModelForm):
    class Meta:
        model = Faculte
        fields = ['libelle',]
        widgets = {
            'libelle': forms.TextInput(attrs={'class':'form-control'}),

        }
    