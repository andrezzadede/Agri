from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento, Estado
from .forms import EventoForm
from django.db.models import Count

def estado_list(request):
    eventos = Evento.objects.all()
    return render(request, 'list_estado.html', {'eventos': eventos})

def eventos_list(request):
    eventos = Evento.objects.all()
    return render(request, 'evento_list.html', {'eventos': eventos})

def eventos_new(request):
    form = EventoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('evento_list')
    return render(request, 'evento_form.html', {'form': form})


def eventos_update(request, id):
    evento = get_object_or_404(Evento, pk=id)
    form = EventoForm(request.POST or None, request.FILES or None, instance=evento)
    if form.is_valid():
        form.save()
        return redirect('evento_list')
    return render(request, 'evento_form.html', {'form': form})


def eventos_delete(request, id):
    evento = get_object_or_404(Evento, pk=id)
    form = EventoForm(request.POST or None, request.FILES or None, instance=evento)
    if request.method == 'POST':
        evento.delete()
        return redirect('evento_list')
    return render(request, 'confirm_del_even.html', {'form': form})




