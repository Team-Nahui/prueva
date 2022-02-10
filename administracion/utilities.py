from .pedidosOnMap import PedidoLocation
from .models import Pedido
from django.shortcuts import get_object_or_404


def check_pedido_state(pedido):
    """
    Este medodo verifica el estado del pedido
    """
    if pedido.estado == 'pendiente':
        correct = True
    else:
        correct = False
    return correct


def check_pedido_is_marked(pedido):
    """ Este medto verifica si el pedido ya esta marcado en el mapa"""
    list_pedidos_marked = PedidoLocation.get_list_pedidos()
    marked = None

    for pedido_aux in list_pedidos_marked:
        if pedido.id == pedido_aux.id:
            marked = True
        else:
            marked = False

    return marked


def get_hour_to_date(date):
    """
    Obtenemos la hora de una fecha y lo devolvemos
    """
    hour = f'{date.hour}: {date.minute}: {date.second}'
    return hour




