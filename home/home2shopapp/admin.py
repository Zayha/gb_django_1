from django.contrib import admin
from .models import Client, Product, OrderProduct, Order


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'tel_number', 'address']
    ordering = ['-creation_date']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'art', 'title', 'unit_price', 'qty', 'is_visible']
    list_display_links = ['id', 'art', 'title']
    list_filter = ['qty']
    ordering = ['id', '-qty']
    list_editable = ['is_visible']
    readonly_fields = ['creation_date', 'modified_date']
    actions = ['reset_qty']
    search_fields = ['title', 'description']
    search_help_text = "Поиск по полям Наименование и Описание"

    def reset_qty(self, request, queryset):
        queryset.update(qty=0)

    reset_qty.short_description = 'Обнулить количество товаров'

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['art', 'title'],
            },
        ), (
            'Описание товара',
            {
                'classes': ['collapse'],
                'fields': ['description'],
            },
        ), (
            'Параметры товара',
            {
                'classes': ['wide'],
                'fields': ['unit_price', 'qty', 'is_visible', 'photo'],
            },
        ), (
            'Даты',
            {
                'classes': ['collapse'],
                'fields': ['creation_date', 'modified_date'],
            },
        ),
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'is_visible']
    list_editable = ['is_visible', 'client']
    readonly_fields = ('display_total_price',)

    def display_total_price(self, obj):
        return obj.calculate_total_price()

    display_total_price.short_description = 'Total Price'


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'products', 'order', 'qty']
    search_fields = ['order']
    search_help_text = 'Поиск по графе Заказ'
    ordering = ['order']
    list_filter = ['order']


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)
admin.site.register(Order, OrderAdmin)
