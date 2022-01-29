from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', HomeView.as_view(), name='home_admin'),

    # Producto urls
    path('producto/', ProductoListView.as_view(), name='listar_productos'),
    path('producto/crear/', CreateProductoView.as_view(), name='crear_producto'),
    path('producto/editar/<int:pk>', EditProductoView.as_view(), name='editar_producto'),
    path('producto/detalle/<int:pk>', ProductoDetailView.as_view(), name='producto_detalle'),
    path('producto/eliminar/<int:pk>', ProductoDeleteView.as_view(), name='eliminar_producto'),

    # Oferta Urls
    path('oferta/', OfertaListView.as_view(), name='listar_ofertas'),
    path('oferta/crear/', CreateOfertaView.as_view(), name='crear_oferta'),
    path('oferta/editar/<int:pk>', EditOfertaView.as_view(), name='editar_oferta'),
    path('oferta/detalle/<int:pk>', OfertaDetailView.as_view(), name='oferta_detalle'),

    # Categoria Urls
    path('categoria/', CategoriaListView.as_view(), name='listar_categoria'),
    path('categoria/crear/', CategoriaCreateView.as_view(), name='crear_categoria'),
    path('categoria/<int:pk>/editar/', CategoriaEditView.as_view(), name='editar_categoria'),
    path('categoria/<int:pk>/detalle/', CagetgoriaDetailView.as_view(), name='ver_categoria'),
    path('categoria/<int:pk>/eliminar/', CategoriaDeleteView.as_view(), name='eliminar_categoria')


]