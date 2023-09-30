from django.urls import path
from persona.api.views import guardarPersona, clienteView, MascotaCreate, ClienteVerificacion,CambiarContraseña, CorreoPassword

urlpatterns = [
    path('guardar_cliente/',guardarPersona.as_view()),
    path('ver_clientes/',clienteView.as_view()),
    path('mascota_crear/',MascotaCreate.as_view()),
    path('verificacion/', ClienteVerificacion.as_view()),
    path('password/', CambiarContraseña.as_view()),
    path('correo_pass', CorreoPassword.as_view()),
]