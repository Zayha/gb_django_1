from django.http import HttpResponse
from django.shortcuts import render

from .models import Product


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
