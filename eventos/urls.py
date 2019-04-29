from django.urls import path
from .views import eventos_list
from .views import eventos_new
from .views import eventos_update
from .views import eventos_delete
from .views import estado_list

urlpatterns = [
    path('list/', eventos_list, name="evento_list"), 
    path('new/', eventos_new, name="evento_new"),
    path('update/<int:id>', eventos_update, name="eventos_update"),
    path('delete/<int:id>', eventos_delete, name="eventos_delete"),
    path('estado_list/', estado_list, name="estado_list"),
]