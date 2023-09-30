from rest_framework import serializers
from comercio.models import Producto, Pedido, Pedido_X_Producto

class ProductoViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = ['nombre','precio','descripcion','imagen']

class PedidoViewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pedido
        fields = ['fecha','estado','tipo_entrega','total']


class CreatePedido(serializers.ModelSerializer):

    class Meta:
        model = Pedido
        fields = ['tipo_entrega','total', 'cliente_idCliente']

    # def create(self, validated_data):
    #     productos_data = validated_data.pop('productos')
    #     pedido = Pedido_X_Producto.objects.create(**validated_data)
    #     for producto_data in productos_data:
    #         ProductoxPedidoSerializer.objects.create(pedido=pedido, **producto_data)
    #     return pedido      

class ProductoxPedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pedido_X_Producto
        fields = ['producto_idProducto','cantidad']
       

class ProductoCreate(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = '__all__'  