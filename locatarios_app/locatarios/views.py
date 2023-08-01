from django.shortcuts import render, redirect
from .models import Locatario
from .forms import LocatarioForm

def lista_locatarios(request):
    locatarios = Locatario.objects.all()
    return render(request, 'lista_locatarios.html', {'locatarios': locatarios})

def adicionar_locatario(request):
    if request.method == 'POST':
        form = LocatarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_locatarios')
    else:
        form = LocatarioForm()
    return render(request, 'adicionar_locatario.html', {'form': form})