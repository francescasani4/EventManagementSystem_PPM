from django.urls import path
from . import views

app_name = 'evento'

urlpatterns = [
    path('', views.index, name='index'),
]