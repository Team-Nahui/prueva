class PedidoLocation:
    """
    Esta clase maneja los pedidos a mostrar en el mapa de localizacion de pedidos
    """
    _pedidos = []

    def __init__(self, id_pedido, lat_pedido, long_pedido):
        self.id = id_pedido
        self.latitud = lat_pedido
        self.longitud = long_pedido

    @classmethod
    def get_list_pedidos(cls):
        return cls._pedidos

    @classmethod
    def add_pedido(cls, pedido):
        if pedido in cls._pedidos:
            return f'EL pedido con id: {pedido.id} ya esta registrado'
        else:
            cls._pedidos.append(pedido)

    @classmethod
    def print_pedidos_map(cls):
        print('Lista de pedidos')
        if len(cls._pedidos) == 0:
            print('No hay pedidos a mostrar en el mapa')
        else:
            for pedido in cls._pedidos:
                print(f'Id: {pedido.id}, lat: {pedido.latitud}, long: {pedido.longitud}')

    @classmethod
    def remove_pedido(cls, pedido):
        if pedido in cls._pedidos:
            cls._pedidos.remove(pedido)
        else:
            return 'Pedido no esta en el mapa'

    @classmethod
    def list_peditos_to_empty(cls):
        cls._pedidos = []

    def __str__(self):
        return f'Id: {self.id}, lat: {self.latitud}, long: {self.longitud}'

