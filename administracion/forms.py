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
        fields = '__all__'
        widgets = {
            'fechaInicio': forms.DateTimeInput,
            'fechaFin': forms.DateTimeInput,
        }
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
        fields = '__all__'
        exclude = []
        widgets = {
            'hora_pedido': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo_transaccion': forms.TextInput(attrs={'class': 'form-control'}),
            'latitud': forms.TextInput(attrs={'class': 'form-control'}),
            'longitud': forms.TextInput(attrs={'class': 'form-control'}),
            'latitud_origen': forms.TextInput(attrs={'class': 'form-control'}),
            'longitud_origen': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'evaluacion': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'total': forms.TextInput(attrs={'class': 'form-control'}),
            'precioDelivery': forms.TextInput(attrs={'class': 'form-control'}),
            'tipoPago': forms.TextInput(attrs={'class': 'form-control'}),
            'tipoDocpago': forms.Select(attrs={'class': 'form-control'}),
            'docPago': forms.Textarea(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
        }


class PedidoEditLocationForm(forms.ModelForm):
    """
    Formulario para editar la localizacion del pedido
    """
    class Meta:
        model = Pedido
        fields = ['latitud', 'longitud']
        widgets = {
            'latitud': forms.TextInput(attrs={'class': 'form-control'}),
            'longitud': forms.TextInput(attrs={'class': 'form-control'})
        }


class PedidoPayForm(forms.ModelForm):
    """
    Formulario para pagar el pedido
    """
    class Meta:
        model = Pedido
        fields = ['tipoPago', 'tipoDocpago', 'docPago']
        widgets = {
            'tipoPago': forms.TextInput(attrs={'class': 'form-control'}),
            'tipoDocpago': forms.Select(attrs={'class': 'form-control'}),
            'docPago': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        exclude = []
