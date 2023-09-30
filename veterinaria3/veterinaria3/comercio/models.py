from django.db import models
from persona.models import Cliente

class Pedido(models.Model):
    idpedido = models.AutoField(primary_key=True)
    fecha = models.DateField()
    estado = models.CharField(max_length=45)
    tipo_entrega=models.CharField(max_length=45)
    total = models.FloatField()
    cliente_idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)


class Producto(models.Model):
    idproducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    descripcion = models.CharField(max_length=150)
    stock = models.IntegerField()
    imagen = models.CharField(max_length=240)


class Pedido_X_Producto(models.Model):
    id = models.AutoField(primary_key=True)
    producto_idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido_idPedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)