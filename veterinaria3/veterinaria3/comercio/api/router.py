from django.urls import path
from comercio.api.views import ProductoView, PedidoViewCliente

urlpatterns =[
    path('mostrar_producto', ProductoView.as_view()),
    path('pedido_cliente', PedidoViewCliente.as_view()),
]