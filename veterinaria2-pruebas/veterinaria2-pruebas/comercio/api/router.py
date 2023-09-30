from django.urls import path
from comercio.api.views import ProductoView, PedidoViewCliente,CrearCheckout, GenerarPedido, CrearProducto

urlpatterns =[
    path('mostrar_producto', ProductoView.as_view()),
    path('crear_producto/', CrearProducto.as_view()),
    path('pedido_cliente', PedidoViewCliente.as_view()),
    path('pago/',CrearCheckout.as_view()),
    path('generar_pedido/',GenerarPedido.as_view()),
]