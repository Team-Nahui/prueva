from django.contrib import admin
from .models import Pedido, Producto, Oferta, Categoria

# Register your models here.
admin.site.register(Pedido)
admin.site.register(Producto)
admin.site.register(Oferta)
admin.site.register(Categoria)