from django.urls import path
from persona.api.views import guardarPersona, clienteView, MascotaCreate

urlpatterns = [
    path('guardar_cliente/',guardarPersona.as_view()),
    path('ver_clientes/',clienteView.as_view()),
    path('mascota_crear/',MascotaCreate.as_view()),
]