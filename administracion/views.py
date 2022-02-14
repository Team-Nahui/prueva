from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .models import Producto, Oferta, Categoria, Pedido, Operacion, Tags
from .forms import ProductoForm, OfertaForm, CategoriaForm, PedidoForm, PedidoEditLocationForm, OperacionForm, TagsForm
from .pedidosOnMap import PedidoLocation
from .utilities import check_pedido_state, check_pedido_is_marked, get_hour_to_date
import json


class pruebaView(View):

    def get(self, request):
        context = {
            'productos': Producto.objects.all(),
        }
        return render(request, 'administracion/ejemplo_extendBase.html', context)


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
            'message': '',
            'state': 'create',
            'button_text': 'Agregar',
        }
        return render(request, 'administracion/producto_new_add_template.html', context)

    def post(self, request):
        """
        Crea un nuevo producto
        :param request: HttpRequest
        :return: HttpResponse
        """
        success_messages = ''
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el objeto producto y me lo devuelves
            form = ProductoForm()
            success_messages = 'Producto creado con exito!'
        context = {
            'form': form,
            'message': success_messages,
            'state': 'create',
            'button_text': 'Agregar',
        }
        return render(request, 'administracion/producto_new_add_template.html', context)


class EditProductoView(View):
    def get(self, request, pk):
        # llenamos los campos del formulario producto  con los datos del producto seleccionado
        producto = get_object_or_404(Producto, id=pk)
        # form = ProductoForm(initial={
        #     'descripcion': producto.descripcion,
        #     'cantidad': producto.cantidad,
        # })
        form = ProductoForm(instance=producto)
        context = {
            'form': form,
            'message': '',
            'state': 'edit',
            'button_text': 'Guardar cambios'
        }
        return render(request, 'administracion/producto_new_add_template.html', context)

    def post(self, request, pk):
        success_message = ''
        producto = get_object_or_404(Producto, id=pk)
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            success_message = 'Actualizacion guardado con exito'
        context = {
            'form': form,
            'message': success_message,
            'state': 'Edit',
            'button_text': 'Guardar cambios',
        }
        return render(request, 'administracion/producto_new_add_template.html', context)


class ProductoDetailView(View):
    def get(self, request, pk):
        """
         Muestra todos los datos del producto
         """
        contex = {
            'producto': get_object_or_404(Producto, id=pk)
        }
        return render(request, 'administracion/producto_detalle.html', contex)


class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = reverse_lazy('listar_productos')


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
        form = OfertaForm()
        context = {
            'form': form,
            'message': '',
            'state': 'create',
            'button_text': 'Crear Oferta',
        }
        return render(request, 'administracion/oferta_create.html', context)

    def post(self, request):
        """
        Crear una nueva oferta y muestra en mensaje
        """
        success_message = ''
        form = OfertaForm(request.POST)
        if form.is_valid():
            form.save()
            form = OfertaForm()
            success_message = 'Guardado con exito!'
        contex = {
            'form': form,
            'message': success_message,
            'state': 'create',
            'button_text': 'Crear Oferta',
        }
        return render(request, 'administracion/oferta_create.html', contex)


class EditOfertaView(View):
    def get(self, request, pk):
        """
        Pinta el formulario con los datos de la oferta seleccionada
        """
        oferta = get_object_or_404(Oferta, id=pk)
        form = OfertaForm(instance=oferta)

        context = {
            'form': form,
            'message': '',
            'state': 'edit',
            'button_text': 'Guardar Canmbios',
        }
        return render(request, 'administracion/oferta_create.html', context)

    def post(self, request, pk):
        success_message = ''
        oferta = get_object_or_404(Oferta, id=pk)
        form = OfertaForm(request.POST, instance=oferta)
        if form.is_valid():
            form.save()
            success_message = 'Actualizacion guardado con exito'
        context = {
            'form': form,
            'message': success_message,
            'state': 'edit',
            'button_text': 'Guardar Canmbios',
        }
        return render(request, 'administracion/oferta_create.html', context)


class OfertaDetailView(View):
    def get(self, request, pk):
        # oferta = Oferta.objects.filter(pk=pk)
        context = {
            'oferta': get_object_or_404(Oferta, id=pk),
        }
        return render(request, 'administracion/oferta_detalle.html', context)


class OfertadeleteView(DeleteView):
    model = Oferta
    success_url = reverse_lazy('listar_ofertas')


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
            'message': '',
            'state': 'create',
            'button_text': 'Agregar',
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
            'state': 'create',
            'button_text': 'Agregar',
        }
        return render(request, 'administracion/categoria_create.html', context)


class CategoriaEditView(View):
    def get(self, request, pk):
        """ Muestra el formulario para categoria"""
        form = CategoriaForm(instance=get_object_or_404(Categoria, id=pk))
        context = {
            'form': form,
            'message': '',
            'state': 'edit',
            'button_text': 'Guardar cambios',
        }
        return render(request, 'administracion/categoria_create.html', context)

    def post(self, request, pk):
        """
        Edita una categoria y lo guarda
        """
        success_message = ''
        categoria = get_object_or_404(Categoria, id=pk)
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            success_message = 'Actualizacion cuardado con exito'

        context = {
            'form': form,
            'message': success_message,
            'state': 'edit',
            'button_text': 'Guardar cambios',
        }
        return render(request, 'administracion/categoria_create.html', context)


class CagetgoriaDetailView(View):
    def get(self, request, pk):
        """
        muesta todos los campos de categoria
        """
        categoria = get_object_or_404(Categoria, id=pk)
        context = {
            'categoria': categoria
        }
        return render(request, 'administracion/categoria_detail.html', context)


class CategoriaDeleteView(DeleteView):
    model = Categoria
    success_url = reverse_lazy('listar_categoria')


class PedidoListView(View):
    def get(self, request):
        pendind_orders = Pedido.objects.all().filter(estado='pendiente')
        PedidoLocation.list_peditos_to_empty()
        for order in pendind_orders:
            client = order.cliente
            new_order_to_map = PedidoLocation(order.id,
                                              order.latitud,
                                              order.longitud,
                                              get_hour_to_date(order.hora_pedido),
                                              f'{client.nombres} {client.apellidos}',
                                              client.telefono)
            PedidoLocation.add_pedido(new_order_to_map)
        pedidos_map = PedidoLocation.list_to_json()
        context = {
            'pedidos': Pedido.objects.all(),
            'message': '',
            'pedidos_map_json': json.dumps(pedidos_map, indent=len(pedidos_map))
        }
        return render(request, 'administracion/pedido_admin.html', context)


class PedidoCreateView(View):
    def get(self, request):
        """ Muestra el formulario para pedido"""
        form = PedidoForm()
        context = {
            'form': form,
            'message': '',
            'state': 'create',
            'button_text': 'Agregar',
        }
        return render(request, 'administracion/pedido_create.html', context)

    def post(self, request):
        """
        crear un pedido y lo guarda
        """
        success_message = ''
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            form = PedidoForm()
            success_message = 'Pedido creado con exito'

        context = {
            'form': form,
            'message': success_message,
            'state': 'create',
            'button_text': 'Agregar',
        }
        return render(request, 'administracion/pedido_create.html', context)


class PedidoEditView(View):
    def get(self, request, pk):
        """ Muestra el formulario para categoria"""
        form = PedidoForm(instance=get_object_or_404(Pedido, id=pk))
        context = {
            'form': form,
            'message': '',
            'state': 'edit',
            'button_text': 'Guardar cambios',
        }
        return render(request, 'administracion/pedido_create.html', context)

    def post(self, request, pk):
        """
        Edita una categoria y lo guarda
        """
        success_message = ''
        pedido = get_object_or_404(Pedido, id=pk)
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            success_message = 'Cambios cuardado con exito'

        context = {
            'form': form,
            'message': success_message,
            'state': 'edit',
            'button_text': 'Guardar cambios',
        }
        return render(request, 'administracion/pedido_create.html', context)


class PedidoDetailView(View):
    def get(self, request, pk):
        """
        Muestra los datos del pedido
        """
        pedido = get_object_or_404(Pedido, id=pk)
        context = {
            'pedido': pedido,
        }
        return render(request, 'administracion/pedido_detail.html', context)


class PedidoDeleteView(View):
    def get(self, request, pk):
        pedido = get_object_or_404(Pedido, id=pk)
        context = {
            'pedido': pedido
        }
        return render(request, 'administracion/pedido_delete.html', context)

    def post(self, request, pk):
        get_object_or_404(Pedido, id=pk).delete()
        return redirect('listar_pedido')


# Caso de uso Mostrar ubicacion de Pedidos
class PedidoEditLocationView(View):
    def get(self, request, pk):
        """ Muestra el formulario para categoria"""
        form = PedidoEditLocationForm(instance=get_object_or_404(Pedido, id=pk))
        # Agregamos la locacion del pedido a la lista de pedidos a mostrar en el map
        context = {
            'form': form,
            'pedido': get_object_or_404(Pedido, pk=pk),
            'message': '',
        }
        return render(request, 'administracion/pedido_edit_location.html', context)

    def post(self, request, pk):
        """
        Edita una categoria y lo guarda
        """
        success_message = ''
        pedido = get_object_or_404(Pedido, id=pk)
        form = PedidoEditLocationForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            success_message = 'Cambios cuardado con éxito'

        context = {
            'form': form,
            'pedido': get_object_or_404(Pedido, pk=pk),
            'message': success_message,
        }
        return render(request, 'administracion/pedido_edit_location.html', context)


class PedidoPayView(View):
    def get(self, request, pk):
        """ Muestra el formulario para registrar Operacion"""
        form = OperacionForm()
        context = {
            'form': form,
            'message': '',
        }
        return render(request, 'administracion/pedido_pay.html', context)

    def post(self, request, pk):
        """
        Edita una categoria y lo guarda
        """
        success_message = ''
        pedido = get_object_or_404(Pedido, pk=pk)
        operacion_with_pedido = Operacion()
        operacion_with_pedido.pedido = pedido
        form = OperacionForm(request.POST, instance=operacion_with_pedido)
        if form.is_valid():
            form.save()
            pedido.pagado = True
            pedido.save()
            success_message = 'Pedido pagado y Operacion guardado con éxito'

        context = {
            'form': form,
            'message': success_message,
        }
        return render(request, 'administracion/pedido_pay.html', context)


class LocationMarkeronMapView(View):
    def get(self, request, pk):
        pedido = get_object_or_404(Pedido, pk=pk)
        pedido_state = check_pedido_state(pedido)
        if pedido_state:
            """
            El pedido esta con estado: Pendiente, ocurre dos casos:
            1.- Ya este marcado en y se esta actualizando: Actualizar localizacion
            2.- el pedido aun no este marcado: agregar a los marcadores o pedidos en seguimiento
            """
            pedido_is_marked = check_pedido_is_marked(pedido)
            cliente = pedido.cliente
            pedido_to_marker = PedidoLocation(pedido.id,
                                              pedido.latitud,
                                              pedido.longitud,
                                              get_hour_to_date(pedido.hora_pedido),
                                              f'{cliente.nombres} {cliente.apellidos}',
                                              cliente.telefono)
            if pedido_is_marked:
                PedidoLocation.set_pedido_in_list(pedido_to_marker)
            else:
                PedidoLocation.add_pedido(pedido_to_marker)
            return redirect('listar_pedido')
        else:
            return redirect('editar_pedido', pk)


class ClienteDetailView(View):
    def get(self, request, pk):
        pedido = get_object_or_404(Pedido, pk=pk)
        cliente = pedido.cliente
        context = {
            'cliente': cliente,
            'pedido': pedido,
        }
        return render(request, 'administracion/cliente_detail.html', context)


class TagsListView(View):
    def get(self, request):
        """
        Esta vista lista los tags
        """
        tags = Tags.objects.all()
        context = {
            'tags': tags,
            'message': ''
        }
        return render(request, 'administracion/tags_admin.html', context)


class CreateTagsView(View):
    def get(self, request):
        """
        Muesta el formulario de Oferta
        """
        form = TagsForm()
        context = {
            'form': form,
            'message': '',
            'state': 'create',
            'button_text': 'Crear Tag',
        }
        return render(request, 'administracion/tags_create.html', context)

    def post(self, request):
        """
        Crear una nueva oferta y muestra en mensaje
        """
        success_message = ''
        form = TagsForm(request.POST)
        if form.is_valid():
            form.save()
            form = TagsForm()
            success_message = 'Agregado con exito!'
        contex = {
            'form': form,
            'message': success_message,
            'state': 'create',
            'button_text': 'Crear Tag',
        }
        return render(request, 'administracion/tags_create.html', contex)


class EditTagsView(View):
    def get(self, request, pk):
        """ Muestra el formulario para categoria"""
        form = TagsForm(instance=get_object_or_404(Tags, id=pk))
        context = {
            'form': form,
            'message': '',
            'state': 'edit',
            'button_text': 'Guardar cambios',
        }
        return render(request, 'administracion/tags_create.html', context)

    def post(self, request, pk):
        """
        Edita una categoria y lo guarda
        """
        success_message = ''
        tag = get_object_or_404(Tags, id=pk)
        form = TagsForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            success_message = 'Cambio cuardado con exito'

        context = {
            'form': form,
            'message': success_message,
            'state': 'edit',
            'button_text': 'Guardar cambios',
        }
        return render(request, 'administracion/tags_create.html', context)


class DetailTagsView(View):
    def get(self, request, pk):
        """
        muesta todos los campos de categoria
        """
        tag = get_object_or_404(Tags, id=pk)
        context = {
            'tag': tag
        }
        return render(request, 'administracion/tags_detail.html', context)


class DeleteTagsView(DeleteView):
    model = Tags
    success_url = reverse_lazy('listar_tags')


class HomeView(View):
    def get(self, request):
        """
        Esta funcion devuelve el Home de la pagina de administracion
        :param request: HttpRequt
        :return: HttpResponse
        """
        context = {
            'something': 'Algo que mostrar en el Home del panel de administracion',
        }
        return render(request, 'administracion/admin_home.html', context)
