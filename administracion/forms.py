from django import forms
from django.core.exceptions import ValidationError

from .models import Producto, Oferta, Categoria, Pedido


class ProductoForm(forms.ModelForm):
    """
    Formulario para el modelo Producto
    """
    class Meta:
        model = Producto
        fields = '__all__'
        exclude = []


class OfertaForm(forms.ModelForm):
    """
    Formulario para el modelo Oferta
    """
    class Meta:
        model = Oferta
        fields ='__all__'
        labels = {
            'descripcion': 'Descripción',
            'fechaInicio': 'Fecha de inicio',
            'fechaFin': 'Fecha de fin',
            'precioOferta': 'Precio de oferta',
        }
        exclude = []


class PedidoForm(forms.ModelForm):
    """
    Formulario para el modelo Pedido
    """
    class Meta:
        model = Pedido
        exclude = []


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        exclude = []