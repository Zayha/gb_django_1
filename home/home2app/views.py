import random

from django.http import HttpResponse
from .models import HeadsOrTails


# Create your views here.

def bin_choices(request):
    result = random.choices([True, False])[0]
    db_obj = HeadsOrTails(result=result)
    db_obj.save()
    return HttpResponse(f'<h1>{"Орел" if result else "Решка"}</h1>')


def show_statistic(request, n):
    data = HeadsOrTails.statistic(n)
    print(data)
    return HttpResponse(f'{data["Orel"]=}\t,{data["Reshka"]=}\t, {data["n"]=}')
