from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from comercio.api.serializers import ProductoViewSerializer, PedidoViewSerializer
from comercio.models import *

class ProductoView(APIView):
    def get(self,request):
       producto = Producto.objects.all()
       serializer = ProductoViewSerializer(producto, many = True)
        
       return Response(serializer.data)
    
class PedidoView(APIView):
    def get(self,request):
        pedido = Pedido.objects.all()
        serializer = PedidoViewSerializer(pedido, many = True)
        return Response(serializer.data)
    
class PedidoViewCliente(APIView):
    def get(self,request):
        id_cliente = request.query_params['id_cliente']
        pedido = Pedido.objects.filter(cliente_idCliente = id_cliente)
        serializer = PedidoViewSerializer(pedido, many = True)
        return Response(serializer.data)   