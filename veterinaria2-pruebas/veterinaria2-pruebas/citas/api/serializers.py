from rest_framework import serializers
from citas.models import *

class CitaCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cita
        fields = '__all__'

class CitaModificarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cita
        fields = ['id_servicio','id_bloque']