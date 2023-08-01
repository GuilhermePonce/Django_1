from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_locatarios, name='lista_locatarios'),
    path('adicionar/', views.adicionar_locatario, name='adicionar_locatario'),
]