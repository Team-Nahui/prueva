from django.contrib import admin
from .models import Pedido, Producto, Oferta, Categoria, Tags, Cliente, Localidad

# Register your models here.
admin.site.register(Pedido)
admin.site.register(Producto)
admin.site.register(Oferta)
admin.site.register(Categoria)
admin.site.register(Tags)
admin.site.register(Cliente)
admin.site.register(Localidad)
