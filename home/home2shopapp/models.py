from django.db import models


# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(blank=False, verbose_name='Email')
    tel_number = models.CharField(max_length=20, verbose_name='Телефон')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')


class Product(models.Model):
    art = models.CharField(max_length=100, unique=True, verbose_name='Артикул товара')
    title = models.CharField(max_length=200, verbose_name='Наименование товара')
    description = models.TextField(verbose_name='Описание товара')
    unit_price = models.FloatField(verbose_name='Цена товара')
    qty = models.IntegerField(verbose_name='Кол-во товара')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    modified_date = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_visible = models.BooleanField(default=False, verbose_name='Отображать товар')

    def __str__(self):
        return f'id:{self.pk}, артикул:{self.art}, {self.title}, {self.unit_price=}, {self.qty=}, {self.is_visible=}'


class OrderProduct(models.Model):
    # client = models.ForeignKey('Client', verbose_name='Клиент', on_delete=models.CASCADE)
    products = models.ForeignKey('Product', verbose_name='Товар', on_delete=models.DO_NOTHING)
    order = models.ForeignKey('Order', verbose_name='Заказ', on_delete=models.CASCADE)
    qty = models.IntegerField(verbose_name='Кол-во товара в заказе')


class Order(models.Model):
    client = models.ForeignKey('Client', verbose_name='Клиент', on_delete=models.CASCADE)
    products = models.ManyToManyField('Product', through='OrderProduct', verbose_name='Товары в заказе')
    total_price = models.FloatField(verbose_name='Общая сумма заказа')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    modified_date = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_visible = models.BooleanField(default=False, verbose_name='Отображать товар')