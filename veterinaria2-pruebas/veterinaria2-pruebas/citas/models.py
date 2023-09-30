from django.db import models
from persona.models import Cliente

class Servicio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    cupo = models.IntegerField()


class Bloque(models.Model):
    id = models.AutoField(primary_key=True)
    hora = models.CharField(max_length=30)


class Cita(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    id_servicio = models.ForeignKey(Servicio, on_delete= models.CASCADE)
    id_bloque = models.ForeignKey(Bloque, on_delete= models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE)