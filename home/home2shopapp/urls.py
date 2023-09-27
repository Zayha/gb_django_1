from django.urls import path
from .views import show_all, is_visible, del_product, ShowAllOrders, ShowOrderDetails, ShowAllOrdersFromClient, \
    ShowAllProductsFromClient

urlpatterns = [
    path('', show_all, name='show_all'),
    path('iv/', is_visible, name='is_visible'),
    path('del/<int:id_p>', del_product, name='del_product'),
    path('l3/orders/', ShowAllOrders.as_view(), name='all_orders'),
    path('l3/order/<int:pk>', ShowOrderDetails.as_view(), name='order'),
    path('l3/orders/<int:pk>', ShowAllOrdersFromClient.as_view(), name='orders_from_client'),
    path('l3/products/<int:client_id>/<str:period>', ShowAllProductsFromClient.as_view(), name='show_products')
]