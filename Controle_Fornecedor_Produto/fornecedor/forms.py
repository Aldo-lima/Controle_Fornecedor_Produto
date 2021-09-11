from django import forms
from .models import Fornecedor, Contato


class ForncedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'