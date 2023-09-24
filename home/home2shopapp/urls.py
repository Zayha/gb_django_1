from django.urls import path
from .views import show_all, is_visible, del_product

urlpatterns = [
    path('', show_all, name='show_all'),
    path('iv/', is_visible, name='is_visible'),
    path('del/<int:id_p>', del_product, name='del_product'),
]