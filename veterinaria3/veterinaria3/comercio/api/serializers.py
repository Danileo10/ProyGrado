from rest_framework import serializers
from comercio.models import Producto, Pedido

class ProductoViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = ['nombre','precio','descripcion','imagen']

class PedidoViewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pedido
        fields = ['fecha','estado','tipo_entrega','total']