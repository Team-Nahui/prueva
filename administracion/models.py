from django.db import models
from django.contrib.auth.models import User
# from django.utils.translation import ugettext as _
from django.utils.translation import gettext_lazy as _


class Localidad(models.Model):
    nombre = models.CharField(max_length=50)
    latitud = models.CharField(max_length=20)
    longitud = models.CharField(max_length=20)

    def __str__(self):
        return "%s " % (self.nombre)


class Cliente(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=60)
    creadoEn = models.DateTimeField(auto_now_add=True)
    modificadoEn = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    direccion = models.TextField(null=True)
    documento = models.CharField(max_length = 13, null=True, blank=True)
    telefono = models.CharField(max_length = 9, null=True)
    redSocial = models.CharField(default='0', max_length=15)
    activado = models.BooleanField(default=False)
    codigo = models.CharField(max_length=4,null=True)
    actualizacion = models.BooleanField(default=False)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='clientes')
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE, related_name='Localidad',blank=True, null=True)
    
    def __str__(self):
        return "%s %s" % (self.nombres, self.apellidos)

    class Meta:
        permissions = (
            ('is_negocio', _('Es Negocio')),
            ('is_establecimiento', _('Es Establecimiento')),
            ('is_repartidor', _('Es Repartidor')),
        )


class Sancion(models.Model):
    fechaInicio = models.DateTimeField()
    fechaFin = models.DateTimeField()
    activo = models.BooleanField(blank=True,default=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)


class Perfil(models.Model):
    PERFIL_EMP = (
        (1, 'Administrador'),
        (2, 'Negocio'),
        (3, 'Establecimiento'),
        (4, 'Repartidor'),
        (5, 'Cliente'),
    )
    perfil = models.IntegerField(blank=True, null=True,default=2, choices=PERFIL_EMP)
    estado = models.BooleanField(blank=True,default=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=40)
    imagen = models.ImageField(blank=True, upload_to='producto/categoria/%Y/%m/%d/%I/%M/%S/%p', default='producto/default.jpg')
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nombre}'


class Tags(models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.nombre}'


class Producto(models.Model):
    TIPO_PRODUCTO = (
        ('comida', 'Comida'),
        ('noPerecible', 'No perecible')
    )
    imagen = models.ImageField(blank=True, upload_to='producto/%Y/%m/%d/%I/%M/%S/%p', default='producto/default.jpg')
    descripcion = models.CharField(max_length=100)
    detalles = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=12, choices=TIPO_PRODUCTO)
    precio = models.IntegerField()
    precio_compra = models.IntegerField(null=True)
    creadoEn = models.DateTimeField(auto_now_add=True)
    modificadoEn = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    # establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null = True)
    tags = models.ManyToManyField(Tags)
    puntuacion = models.IntegerField(default=0,null=True)
    vista = models.CharField(max_length=100, default=0)
    cantidad = models.IntegerField(default=0, null=True)

    def __str__(self):
        return '%s' % self.descripcion


class Oferta(models.Model):
    descripcion = models.CharField(max_length=40)
    fechaInicio = models.DateTimeField()
    fechaFin = models.DateTimeField()
    precioOferta = models.IntegerField()
    activo = models.BooleanField(blank=True,default=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)


class ProductoCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    visita = models.IntegerField()


class Pedido(models.Model):
    ESTADO_PEDIDO = (
        ('pendiente', 'Pendiente'),
        ('visto', 'Visto'),
        ('preparado', 'Preparado'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado')
    )
    EVALUACION_PEDIDO = (
        (1, 'Muy malo'),
        (2, 'Malo'),
        (3, 'Medianamente bueno'),
        (4, 'Bueno'),
        (5, 'Excelente')
    )
    TIPODOC_PAGO = (
        (1,'Boleta'),
        (2,'Factura')
        )
    hora_pedido = models.DateTimeField(auto_now_add=True)
    codigo_transaccion = models.CharField(max_length=100, null=True)
    pagado = models.BooleanField(default=False)
    latitud = models.CharField(max_length=20)
    longitud = models.CharField(max_length=20)
    latitud_origen = models.CharField(max_length=20, null=True)
    longitud_origen = models.CharField(max_length=20, null=True)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    evaluacion = models.IntegerField(choices=EVALUACION_PEDIDO, null=True)
    estado = models.CharField(max_length=9, choices=ESTADO_PEDIDO, default='pendiente')
    creadoEn = models.DateTimeField(auto_now_add=True)
    modificadoEn = models.DateTimeField(auto_now=True)
    total = models.CharField(null=True, max_length=20)
    precioDelivery = models.CharField(null=True, max_length=20)
    # player_id = models.CharField(null=True, max_length=100)
    tipoPago = models.CharField(null=True, max_length=20)
    tipoDocpago = models.IntegerField(choices=TIPODOC_PAGO, default=1)
    docPago = models.TextField(null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    #repartidor = models.ForeignKey(Repartidor, on_delete=models.CASCADE, null=True)
    #negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE, null=True)
    productos = models.ManyToManyField(Producto, through="Detalle_pedido")
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return '%s %s %s' % (self.hora_pedido, self.direccion, self.cliente)


class Detalle_pedido(models.Model):
    cantidad = models.IntegerField()
    descripcion = models.TextField(null=True)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='pedidos')

    def __str__(self):
        return '%s %s %s' % (self.producto, self.pedido, self.cantidad)


class Log_cambio_estado(models.Model):
    pendiente = models.DateTimeField(auto_now_add=True)
    visto = models.DateField(null=True)
    preparado = models.DateField(null=True)
    enviado = models.DateField(null=True)
    entregado = models.DateField(null=True)


class Pedido_llamada(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)


class Operacion(models.Model):
    TIPO_PAGO = (
        (1,'Efectivo'),
        (2, 'Electrónico'),
        (3, 'Transferencia'),
        (4, 'Otro'),
    )
    fecha = models.DateField(auto_now_add=True)
    monto = models.FloatField(null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    recivo_pago = models.FileField(blank=True, upload_to='recivo/%Y/%m/%d/', default='recivo/default.pdf')
    tipo_pago = models.IntegerField(null=True, choices=TIPO_PAGO)
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)

    def __str__(self):
        return f'Fecha: {self.fecha} / Monto: {self.monto} / Pedido: #'

# class Lote(models.Model):
#     """
#     Falta agregar
#     campos"""
#     pass
