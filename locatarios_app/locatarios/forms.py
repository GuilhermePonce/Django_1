from django import forms
from .models import Locatario

class LocatarioForm(forms.ModelForm):
    class Meta:
        model = Locatario
        fields = ['nome', 'endereco', 'telefone']