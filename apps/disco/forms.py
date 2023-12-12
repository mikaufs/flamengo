from django import forms

from .models import Disco, Artista, Selo_Fonografico

class DiscoForm(forms.ModelForm):
    class Meta:
        model = Disco
        fields = ['nome', 'descricao', 'ano', 'pais', 'genero', 'quantidade', 'selo_fonografico', 'artistas', 'preco']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'ano': forms.NumberInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.TextInput(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'selo_fonografico': forms.Select(attrs={'class': 'form-control'}),
            'artistas': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
        }