from django.urls import path
from citas.api.views import *

urlpatterns = [
    path('guardar_cita/', CreateCita.as_view()),

]