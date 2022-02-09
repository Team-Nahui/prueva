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
    def add_pedido(cls, new_pedido):
        """
        este metodo agrega un nuevo marcador, si ya existe el marcador en el mapa lo actualiza
        """
        founded = False
        for pedido in cls._pedidos:
            if pedido.id == new_pedido.id:
                founded = True
        if founded:
            return f'EL pedido con id: {new_pedido.id} ya esta registrado'
        else:
            cls._pedidos.append(new_pedido)
            return cls._pedidos

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

    @classmethod
    def list_to_json(cls):
        data = []
        json_list = {}
        if len(cls._pedidos) > 0:
            for pedido in cls._pedidos:
                aux = {'id': pedido.id, 'lat': pedido.latitud, 'lng': pedido.longitud}
                data.append(aux)
            json_list = {'pedidos': data}

        return json_list

