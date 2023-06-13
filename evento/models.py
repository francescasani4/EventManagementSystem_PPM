import datetime
from PIL import Image

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def event_image_upload_path(istance, filename):
    return f'{filename}'

class Evento(models.Model):
    titolo = models.CharField(max_length=100, primary_key=True)
    descrizione = models.TextField()
    data = models.DateField()
    orario = models.TimeField(default=datetime.time)
    luogo = models.CharField(max_length=100)
    programma = models.TextField(default='Non disponibile')
    immagine = models.ImageField(upload_to='event_image_upload_path', null=True, blank=True)
    categoria = models.ManyToManyField('Categoria', related_name='evento', default=None)
    partecipanti = models.ManyToManyField(User, related_name="iscritti_evento")
    utente_creatore = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creatore_evento')
    capienza_massima = models.PositiveIntegerField(default=100000000)
    posti_disponibili = models.PositiveIntegerField(default=100000000)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventi"

    def __str__(self):
        return self.titolo


class Categoria(models.Model):
    tipo = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorie"

    def __str__(self):
        return self.tipo


class Registrazioni(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='registrazione')
    utente = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.utente.username} - {self.evento.titolo}"

    class Meta:
        verbose_name = "Registrazione"
        verbose_name_plural = "Registrazioni"
