from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    # PrimerAPP URLS
    path('producto/', ProductosListView.as_view(), name='listar_productos'),
    path('producto/crear/', CreateProductoView.as_view(), name='crear_producto'),
    path('producto/editar/<int:pk>', EditProductoView.as_view(), name='editar_producto'),
    path('', HomeView.as_view(), name='home_admin'),


]