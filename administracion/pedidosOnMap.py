class PedidoLocation:
    """
    los pedidos en el mapa solo seran los pedidos con estado pendiente
    Esta clase maneja los pedidos a mostrar en el mapa de localizacion de pedidos
    """
    _pedidos = []

    def __init__(self, id_pedido, lat_pedido, long_pedido, hora_pedido, cliente, contacto_cliente):
        self.id = id_pedido
        self.latitud = lat_pedido
        self.longitud = long_pedido
        self.hora_pedido = hora_pedido
        self.cliente = cliente
        self.contacto_cliente = contacto_cliente

    @classmethod
    def get_list_pedidos(cls):
        return cls._pedidos

    @classmethod
    def add_pedido(cls, new_pedido):
        """
        este metodo agrega un nuevo marcador, si ya existe el marcador en el mapa lo actualiza
        """
        marked_onmap = False
        for pedido in cls._pedidos:
            if pedido.id == new_pedido.id:
                marked_onmap = True
        if marked_onmap:
            return 'actualizar'
        else:
            cls._pedidos.append(new_pedido)
            return 'agregado'


    @classmethod
    def set_pedido_in_list(cls, pedido):
        """
        Solo se actualiza la latitud y longitud, los otros campos no
        """
        for pedido_aux in cls._pedidos:
            if pedido.id == pedido_aux.id:
                pedido_aux.latitud = pedido.latitud
                pedido_aux.longitud = pedido.longitud
        return 'done'


    @classmethod
    def print_pedidos_map(cls):
        if len(cls._pedidos) == 0:
            print('No hay pedidos a mostrar en el mapa')
        else:
            for pedido in cls._pedidos:
                print(f'Id: {pedido.id}, lat: {pedido.latitud}, long: {pedido.longitud}')

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
                aux = {'id': pedido.id,
                       'lat': pedido.latitud,
                       'lng': pedido.longitud,
                       'hora_pedido': pedido.hora_pedido,
                       'cliente': pedido.cliente,
                       'contacto_cliente': pedido.contacto_cliente,
                       }
                data.append(aux)
            json_list = {'pedidos': data}

        return json_list

    def to_json(self):
        pedido_json = {
            'id': self.id,
            'lat': self.latitud,
            'lng': self.longitud,
            'hora_pedido': self.hora_pedido,
            'cliente': self.cliente,
            'contacto_cliente': self.contacto_cliente,
        }
        return {'pedido': pedido_json}

