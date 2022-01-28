from django.shortcuts import render
from django.urls import reverse
# Create your views here.
from django.views import View
from .models import Producto, Oferta, Categoria
from .forms import ProductoForm, OfertaForm, CategoriaForm


class ProductoListView(View):

    def get(self, request):
        context = {
            'productos': Producto.objects.all(),
        }
        return render(request, 'administracion/producto_admin_template.html', context)


class CreateProductoView(View):
    def get(self, request):
        """
        Carga el formulario para producto
        """
        form = ProductoForm
        context = {
            'form': form,
            'message': ''
        }
        return render(request, 'administracion/producto_new_add_template.html', context)

    def post(self, request):
        """
        Crea un nuevo producto
        :param request: HttpRequest
        :return: HttpResponse
        """
        success_messages = ''
        form = ProductoForm()
        if form.is_valid():
            new_producto = form.save()  # Guarda el objeto producto y me lo devuelves
            form = ProductoForm()
            success_messages = 'Guardado con exito!'
        context = {
            'form': form,
            'message': success_messages
        }
        return render(request, 'administracion/producto_new_add_template.html', context)


class EditProductoView(View):
    def get(self, request, pk):
        # llenamos los campos del formulario producto  con los datos del producto seleccionado
        form = ProductoForm()
        context = {
            'form': form,
            'message': ''
        }
        return render(request, 'administracion/producto_new_add_template.html', context)


class ProductoDetailView(View):
    def get(self, request, pk):
        """
         Muestra todos los datos del producto
         """
        # producto = Producto.objects.filter(pk=pk)
        contex = {
            'producto': {'id': 1, 'descripcion': ' Pan integral'}
        }
        return render(request, 'administracion/producto_detalle.html', contex)


class OfertaListView(View):
    def get(self, request):
        """
        Esta vista muestra las ofertas en toda la pantalla
        """
        context = {
            'ofertas': Oferta.objects.all(),
            'message': '',
        }
        return render(request, 'administracion/oferta_admin_template.html', context)


class CreateOfertaView(View):
    def get(self, request):
        """
        Muesta el formulario de Oferta
        """
        form = OfertaForm
        context = {
            'form': form,
            'message': '',
            'state': 'create',
            'button_text': 'Crear Oferta',
        }
        return render(request, 'administracion/new_oferta_template.html', context)

    def post(self, request):
        """
        Crear una nueva oferta y muestra en mensaje
        """
        success_message = ''
        form = OfertaForm()
        if form.is_valid():
            new_oferta = form.save()
            form = OfertaForm()
            success_message = 'Guardado con exito!'
        contex = {
            'form': form,
            'message': success_message
        }
        return render(request, 'administracion/new_oferta_template.html', contex)


class EditOfertaView(View):
    def get(self, request, pk):
        """
        Pinta el formulario con los datos de la oferta seleccionada
        """
        # oferta = Oferta.objects.filter(pk=pk)
        form = OfertaForm()
        context = {
            'form': form,
            'message': '',
            'state': 'edit',
            'button_text': 'Guardar Canbios',
        }
        return render(request, 'administracion/new_oferta_template.html', context)

    def post(self, request, pk):
        success_message = ''
        oferta = Oferta.objects.filter(pk=pk)
        form = OfertaForm(instance=oferta)
        if form.is_valid():
            form.save()
            success_message = 'Modificación guardado con exito!'
        context = {
            'form': form,
            'message': success_message
        }
        return render(request, 'administracion/new_oferta_template.html', context)


class OfertaDetailView(View):
    def get(self, request, pk):
        # oferta = Oferta.objects.filter(pk=pk)
        context = {
            'oferta': {
                'id': 1,
                'activo': 'no',
            }
        }
        return render(request, 'administracion/oferta_detalle.html', context)


class CategoriaListView(View):
    def get(self, request):
        """
        Panel de administracion de Categorias, crear, editar y eliminar
        """
        context = {
            'categorias': Categoria.objects.all(),
            'message': ''
        }
        return render(request, 'administracion/categoria_admin.html', context)


class CategoriaCreateView(View):
    def get(self, request):
        """ Muestra el formulario para categoria"""
        form = CategoriaForm()
        context = {
            'form': form,
            'message': ''
        }
        return render(request, 'administracion/categoria_create.html', context)

    def post(self, request):
        """
        crear una categoria y lo guarda
        """
        success_message = ''
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            form = CategoriaForm()
            success_message = 'Categoria creada con exito'

        context = {
            'form': form,
            'message': success_message,
        }
        return render(request, 'administracion/categoria_create.html', context)


class HomeView(View):
    def get(self, request):
        """
        Esta funcion devuelve el Home de la pagina de administracion
        :param request: HttpRequt
        :return: HttpResponse
        """
        context = {
            'something': 'Algo que mostrar en el Home del panel de administracion'
        }
        return render(request, 'administracion/admin_home.html', context)
