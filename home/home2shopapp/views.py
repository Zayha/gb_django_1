from datetime import timedelta

from django.db.models import Prefetch
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, UpdateView

from .forms import ProductForm, EditImage
from .models import Product, Order, OrderProduct, Client


# Create your views here.
def show_all(request):
    selected_objects = Product.objects.filter(is_visible=True)
    result = ''
    for index, prod in enumerate(selected_objects, start=1):
        result += f"{index}\t{prod}<br>"
    return HttpResponse(f'<h1>Список товаров:</h1>,<h3>{result}</h3>')


def is_visible(request):
    if request.method == 'GET':
        id_param = request.GET.get('id')
        is_visible_param = request.GET.get('is_visible')

        if id_param:
            obj = Product.objects.filter(pk=id_param).first()
            if obj and is_visible_param:
                if is_visible_param.lower() in ['1', 'true']:
                    obj.is_visible = True
                    obj.save()
                    return HttpResponse(f'<h2>{obj}</h2>')
                elif is_visible_param.lower() in ['0', 'false']:
                    obj.is_visible = False
                    obj.save()
                    return HttpResponse(f'<h2>Объект не найден</h2>')


# удаление с подтверждением http://127.0.0.1:8000/h2shop/del/1?confirm=yes
def del_product(request, id_p):
    select_obj = Product.objects.filter(pk=id_p).first()
    if select_obj:
        if request.GET.get('confirm') == 'yes':
            return HttpResponse(f'Запись c id {id_p} удалена из базы')
        else:
            select_obj.is_visible = False
            return HttpResponse(f'Запись c id {id_p} удалена из зоны видимости')
    else:
        return HttpResponse(f'Запись c id {id_p} не удалена, проверьте параметры')


class ShowAllOrders(ListView):
    model = Order
    template_name = 'home2shopapp/orders_all.html'
    context_object_name = 'orders'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Заказы'
        return context


class ShowAllOrdersFromClient(ListView):
    model = Order
    template_name = 'home2shopapp/orders_all.html'
    context_object_name = 'orders'

    def get_queryset(self):
        author_id = self.kwargs['pk']
        return Order.objects.filter(client_id=author_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['title'] = 'Заказы'
        return context


class ShowOrderDetails(DetailView):
    model = Order
    template_name = 'home2shopapp/order.html'
    context_object_name = 'order'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['title'] = f'Заказ №{pk}'
        context['products'] = OrderProduct.objects.filter(order_id=pk)
        return context


class ShowAllProductsFromClient(ListView):
    model = OrderProduct
    template_name = 'home2shopapp/products_time_filter.html'
    context_object_name = 'ordered_products'

    def get_queryset(self):
        client_id = self.kwargs.get('client_id')
        client = Client.objects.filter(pk=client_id).first()
        if client:
            today = timezone.now()
            period = self.kwargs.get('period', 'week')

            if period.lower() == 'week':
                start_date = today - timedelta(days=7)
            elif period.lower() == 'month':
                start_date = today - timedelta(days=30)
            elif period.lower() == 'year':
                start_date = today - timedelta(days=365)
            else:
                start_date = today - timedelta(days=7)

            queryset = OrderProduct.objects.filter(
                order__client=client,
                order__creation_date__gte=start_date,
            ).select_related('products').prefetch_related(
                Prefetch('products', queryset=Product.objects.distinct())
            )
        else:
            queryset = None
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['period'] = self.kwargs.get('period', 'week') if self.kwargs.get('period', 'week') in ["week", "month",
                                                                                                       "year"] else 'week'
        context['title'] = f'Товары за {context["period"]}'
        return context


class EditProduct(UpdateView):
    model = Product
    template_name = 'home2shopapp/show_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('success')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактировать товар'
        return context


class AddPhotoToProduct(UpdateView):
    model = Product
    template_name = 'home2shopapp/show_form.html'
    form_class = EditImage
    success_url = reverse_lazy('success')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактировать изображение товара'
        return context
