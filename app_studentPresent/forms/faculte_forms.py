from django.core import validators
from django import forms
from ..models import *

class faculteRegistration(forms.ModelForm):
    class Meta:
        model = Faculte
        fields = ['nom_fac']
        widgets = {
            'nom_fac': forms.TextInput(attrs={'class':'form-control'}),

        }
    