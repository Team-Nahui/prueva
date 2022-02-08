from django.test import TestCase
from pedidosOnMap import PedidoLocation

# Create your tests here.

pedido1 = PedidoLocation(1, 12, 12)
PedidoLocation.add_pedido(pedido1)
pedido2 = PedidoLocation(2, 12, 12)
PedidoLocation.add_pedido(pedido2)
PedidoLocation.print_pedidos_map()

print(PedidoLocation.add_pedido(pedido1))
print(PedidoLocation.add_pedido(pedido2))

