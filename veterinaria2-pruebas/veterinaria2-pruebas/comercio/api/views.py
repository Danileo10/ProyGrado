from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from comercio.api.serializers import ProductoViewSerializer, ProductoCreate, PedidoViewSerializer, CreatePedido, ProductoxPedidoSerializer
from comercio.models import *
import stripe
from django.conf import settings
from django.db import transaction

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
    
class CrearProducto(APIView):
    @transaction.atomic
    def post(self,request):
        serializer = ProductoCreate(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Producto creado con exito', status=status.HTTP_201_CREATED)
        else :
            return Response(status=status.HTTP_400_BAD_REQUEST)  

class BorrarProducto(APIView):
    def delete(self,request):
        id_producto = request.query_params['id_producto']
        producto = Producto.objects.filter(idproducto = id_producto)
        producto.delete()
        return Response('Producto eliminado')        

class ModificarProducto(APIView):
        @transaction.atomic
        def put(self,request):
            id_producto = request.query_params['id_producto']
            producto = Producto.objects.get(id = id_producto)
            serializer = ProductoCreate(producto,request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response('Producto modificado con exito',status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


stripe.api_key = settings.STRIPE_SECRET_KEY
      
class CrearCheckout(APIView):
    def post(self, request):
        productos = request.data['productos'] 

        line_items = []
        for producto_data in productos:
            id_producto = producto_data['id_producto']
            cantidad = producto_data['cantidad']
            producto = Producto.objects.get(idproducto=id_producto)

            item = {
                "price_data": {
                    "currency": "cop",
                    "unit_amount": int(producto.precio) * 100,
                    "product_data": {
                        "name": producto.nombre,
                    },
                },
                "quantity": cantidad,
            }
            line_items.append(item)

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=line_items,
            mode="payment",
            success_url=settings.PAYMENT_SUCCESS_URL,
            cancel_url=settings.PAYMENT_CANCEL_URL,
        )
        return Response(checkout_session.url)    
    

        
class GenerarPedido(APIView):
    @transaction.atomic
    def post(self,request):
        serializer = CreatePedido(data=request.data)
        productos = request.data['productos']
        if serializer.is_valid(raise_exception=True):
            pedido= serializer.save()
            for i in productos:
                serializer2 = ProductoxPedidoSerializer(data=i)
                if serializer2.is_valid(raise_exception=True):
                    serializer2.save(pedido_idPedido = pedido)
        return Response('Se guardo el pedido', status=status.HTTP_200_OK)            