from django.urls import path
from . import views

app_name = 'evento'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('ListaEventi/', views.lista_eventi, name='lista_eventi'),
    path('DettagliEvento/<str:titolo>/', views.dettagli_evento, name='dettagli_evento'),
    path('Ricerca/', views.cerca_evento, name='cerca_evento'),
    path('Accesso/', views.accesso, name='accesso'),
    path('Registrazione/', views.registrazione, name='registrazione'),
    path('Esci/', views.esci, name='esci'),
    path('CreazioneEvento/', views.crea_evento, name='crea_evento'),
    path('ModificaEvento/<str:titolo>/', views.modifica_evento, name='modifica_evento'),
    path('Negazione/', views.negazione, name='negazione'),
    path('IscrizionePresente/', views.iscrizione_presente, name='iscrizione_presente'),
    path('PostiEsauriti/', views.posti_esauriti, name='posti_esauriti'),
    path('RimuoviEvento/<str:titolo>/', views.rimuovi_evento, name='rimuovi_evento'),
    path('Transazione/<str:titolo>/', views.compra_partecipazione, name='compra_partecipazione'),
    path('Pagato/', views.pagato, name='pagato'),
    path('Profilo/', views.info_profilo, name='info_profilo'),
    path('GestioneEventi/', views.gestione_eventi, name='gestione_eventi'),
    path('CreazioneCategoria/', views.crea_categoria, name='crea_categoria'),
    path('PagamentoInCorso/', views.transazione, name='transazione'),
    path('Rimborsato/', views.rimborso, name='rimborso'),
    path('Rimborso/<str:titolo>/', views.rimuovi_partecipazione, name='rimuovi_partecipazione'),
]