# Generated by Django 4.2.1 on 2023-06-13 21:46

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tipo", models.CharField(max_length=50)),
            ],
            options={
                "verbose_name": "Categoria",
                "verbose_name_plural": "Categorie",
            },
        ),
        migrations.CreateModel(
            name="Evento",
            fields=[
                (
                    "titolo",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("descrizione", models.TextField()),
                ("data", models.DateField()),
                ("orario", models.TimeField(default=datetime.time)),
                ("luogo", models.CharField(max_length=100)),
                ("programma", models.TextField(default="Non disponibile")),
                (
                    "immagine",
                    models.ImageField(
                        blank=True, null=True, upload_to="event_image_upload_path"
                    ),
                ),
                ("capienza_massima", models.PositiveIntegerField(default=100000000)),
                ("posti_disponibili", models.PositiveIntegerField(default=100000000)),
                (
                    "categoria",
                    models.ManyToManyField(
                        default=None, related_name="evento", to="evento.categoria"
                    ),
                ),
                (
                    "partecipanti",
                    models.ManyToManyField(
                        related_name="iscritti_evento", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "utente_creatore",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="creatore_evento",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Evento",
                "verbose_name_plural": "Eventi",
            },
        ),
        migrations.CreateModel(
            name="Registrazioni",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "evento",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="registrazione",
                        to="evento.evento",
                    ),
                ),
                (
                    "utente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Registrazione",
                "verbose_name_plural": "Registrazioni",
            },
        ),
    ]