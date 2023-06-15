from django import forms
from .models import Evento, Categoria
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm

class UtenteForm(UserCreationForm):
    nome = forms.CharField(max_length=100)
    cognome = forms.CharField(max_length=100)
    email = forms.EmailField()
    eta = forms.IntegerField()
    class Meta:
        model = User
        fields = ['username', 'nome', 'cognome', 'eta', 'email', 'password1', 'password2']

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titolo', 'descrizione', 'immagine', 'data', 'orario', 'luogo', 'categoria', 'capienza_massima', 'programma']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['tipo']