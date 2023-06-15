from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Evento, Categoria, Registrazioni
from .forms import UtenteForm, EventoForm, CategoriaForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django import forms

# Create your views here.

def homepage(request):
    eventi = Evento.objects.all()
    return render(request, "homepage.html", {'eventi': eventi})

def lista_eventi(request):
    eventi = Evento.objects.all()
    return render(request, 'lista_eventi.html', {'eventi':eventi})

def dettagli_evento(request, titolo):
    evento = Evento.objects.get(titolo=titolo)
    return render(request, 'dettagli_evento.html', {'evento':evento})

def cerca_evento(request):
    query = request.GET.get('query')
    eventi = Evento.objects.all()
    if query:
        eventi = eventi.filter(titolo__icontains=query) | eventi.filter(categoria__tipo__icontains=query)
    return render(request, 'cerca_evento.html', {'eventi':eventi, 'query':query})

def accesso(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            utente = form.get_user()
            login(request, utente)
            return redirect('evento:info_profilo')
    else:
            form = AuthenticationForm()
    return render(request, "registrazione/accesso.html", {'form':form})

@login_required
def info_profilo(request):
    utente = request.user
    iscritti_evento = utente.iscritti_evento.all()

    return render(request, 'info_profilo.html', {'utente':utente, 'iscritti_evento':iscritti_evento})

def registrazione(request):
    if request.method == 'POST':
        form = UtenteForm(request.POST)
        if form.is_valid():
            utente = form.save()
            login(request, utente)
            return redirect('evento:homepage')
    else:
        form = UtenteForm()
    return render(request, "registrazione/registrazione.html", {'form':form})

def esci(request):
    logout(request)
    return render(request, "registrazione/esci.html")

def negazione(request):
    return render(request, "negazione.html")

def iscrizione_presente(request):
    return render(request, "iscrizione_presente.html")

def posti_esauriti(request):
    return render(request, "posti_esauriti.html")

def compra_partecipazione(request, titolo):
    evento = get_object_or_404(Evento, titolo=titolo)
    iscritto = Registrazioni.objects.filter(evento=evento, utente=request.user).exists()

    if iscritto:
        return redirect('evento:iscrizione_presente')

    if evento.posti_disponibili > 0:
        iscrizione = Registrazioni(evento=evento, utente=request.user)
        iscrizione.save()
        evento.posti_disponibili -= 1
        evento.partecipanti.add(request.user)
        request.user.iscritti_evento.add(evento)
        evento.save()
        return redirect('evento:transazione')
    elif evento.posti_disponibili <= 0:
        return redirect('evento:posti_esauriti')

def rimuovi_partecipazione(request, titolo):
    evento = get_object_or_404(Evento, titolo=titolo)
    iscritto = Registrazioni.objects.filter(evento=evento, utente=request.user).exists()

    if not iscritto:
        return redirect('evento:compra_partecipazione')

    Registrazioni.objects.filter(evento=evento, utente=request.user).delete()
    evento.posti_disponibili += 1
    evento.save()
    evento.partecipanti.remove(request.user)
    request.user.iscritti_evento.remove(evento)
    evento.save()

    return redirect('evento:rimborso')


def pagato(request):
    return render(request, "pagato.html")

def rimborso(request):
    return render(request, "rimborso.html")

@login_required
def crea_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.utente_creatore = request.user
            evento.posti_disponibili = evento.capienza_massima
            evento.save()
            return redirect('evento:lista_eventi')
    else:
        form = EventoForm()

    return render(request, 'crea_evento.html', {'form': form})

@login_required
def modifica_evento(request, titolo):
    evento = get_object_or_404(Evento, titolo=titolo)

    if request.user != evento.utente_creatore:
        return redirect('evento:negazione')

    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES, instance=evento)

        if form.is_valid():
            evento = form.save()
            evento.posti_disponibili = evento.capienza_massima
            evento.save()
            return redirect('evento:homepage')
    else:
        form = EventoForm(instance=evento)

    return render(request, 'modifica_evento.html', {'form':form, 'evento':evento})

@login_required
def rimuovi_evento(request, titolo):
    evento = get_object_or_404(Evento, titolo=titolo)

    if request.user != evento.utente_creatore:
        return redirect('evento:negazione')

    titolo = evento.titolo
    evento.delete()
    return render(request, "rimuovi_evento.html", {'titolo':titolo})

def gestione_eventi(request):
    utente = request.user
    eventi = Evento.objects.filter(utente_creatore=utente)
    return render(request, "gestione_eventi.html", {'eventi':eventi})

def crea_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('evento:crea_evento')
    else:
        form = CategoriaForm()

    return render(request, "crea_categoria.html", {'form': form})

def transazione(request):
    return render(request, "transazione.html")