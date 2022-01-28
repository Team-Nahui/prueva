from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import Producto
from .forms import ProductoForm


class ProductosListView(View):

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
        Crea un nueva foto
        :param request: HttpRequest
        :return: HttpResponse
        """
        success_messages = ''
        producto = Producto()
        form = ProductoForm(request.POST, instance=producto)
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
        #llenamos los campos del formulario producto  con los datos del producto seleccionado
        form = ProductoForm()
        context = {
            'form': form,
            'message': ''
        }
        return render(request, 'administracion/producto_new_add_template.html', context)


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