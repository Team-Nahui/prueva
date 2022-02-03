from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', HomeView.as_view(), name='home_admin'),

    # Producto urls
    path('producto/', ProductoListView.as_view(), name='listar_productos'),
    path('producto/crear/', CreateProductoView.as_view(), name='crear_producto'),
    path('producto/editar/<int:pk>', EditProductoView.as_view(), name='editar_producto'),
    path('producto/detalle/<int:pk>', ProductoDetailView.as_view(), name='ver_producto'),
    path('producto/eliminar/<int:pk>', ProductoDeleteView.as_view(), name='eliminar_producto'),

    # Oferta Urls
    path('oferta/', OfertaListView.as_view(), name='listar_ofertas'),
    path('oferta/crear/', CreateOfertaView.as_view(), name='crear_oferta'),
    path('oferta/editar/<int:pk>', EditOfertaView.as_view(), name='editar_oferta'),
    path('oferta/detalle/<int:pk>', OfertaDetailView.as_view(), name='ver_oferta'),
    path('oferta/<int:pk>/eliminar', OfertadeleteView.as_view(), name='eliminar_oferta'),

    # Categoria Urls
    path('categoria/', CategoriaListView.as_view(), name='listar_categoria'),
    path('categoria/crear/', CategoriaCreateView.as_view(), name='crear_categoria'),
    path('categoria/<int:pk>/editar/', CategoriaEditView.as_view(), name='editar_categoria'),
    path('categoria/<int:pk>/detalle/', CagetgoriaDetailView.as_view(), name='ver_categoria'),
    path('categoria/<int:pk>/eliminar/', CategoriaDeleteView.as_view(), name='eliminar_categoria'),

    # Pedido urls
    path('pedido/', PedidoListView.as_view(), name='listar_pedido'),
    path('pedido/crear/', PedidoCreateView.as_view(), name='crear_pedido'),
    path('pedido/<int:pk>/editar/', PedidoEditLocationView.as_view(), name='editar_pedido'),
    path('pedido/<int:pk>/ver/', PedidoDetailView.as_view(), name='ver_pedido'),
    path('pedido/<int:pk>/eliminar/', PedidoDeleteView.as_view(), name='eliminar_pedido'),
    path('pedido/<int:pk>/pagar/', PedidoPayView.as_view(), name='pagar_pedido'),

    path('prueba/', pruebaView.as_view(), name='prueba'),


]