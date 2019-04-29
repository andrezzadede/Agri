from django.forms import ModelForm
from .models import Evento, Estado

class EventoForm(ModelForm):
    class Meta:
        model = Evento
        fields = ['data', 'cidade', 'estado']

class EstadoForm(ModelForm):
    class Meta:
        model = Estado
        fields = ['estado']

