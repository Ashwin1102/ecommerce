from django.contrib import admin
from django.urls import path
from customers import views as customer_views
from categories import views as categories_views
from products import views as products_views
from django.shortcuts import redirect
from orders import views as orders_views
from orderItems import views as orderItems_views
from carts import views as carts_views
from cartItems import views as cartItems_views

def redirect_to_admin(request):
    return redirect('/admin')

urlpatterns = [
    path('', redirect_to_admin),
    path('admin/', admin.site.urls),
    
    # Customers
    path('customers/', customer_views.customer_list, name='customer-list'),
    path('customers/<int:pk>/', customer_views.customer_get_by_id, name='customer-get-by-id'),
    path('customers/<int:pk>/delete/', customer_views.customer_delete_by_id, name='customer-delete-by-id'),
    path('customers/delete/', customer_views.customer_delete_all, name='customer-delete-all'),

    # Categories
    path('categories/', categories_views.categories_list, name='categories-list'),
    path('categories/<int:pk>/', categories_views.categories_get_by_id, name='categories-get-by-id'),
    path('categories/<int:pk>/delete/', categories_views.categories_delete_by_id, name='categories-delete-by-id'),
    path('categoriess/delete/', categories_views.categories_delete_all, name='categories-delete-all'),

    # Products
    path('products/', products_views.products_list, name='products-list'),
    path('products/<int:pk>/', products_views.products_get_by_id, name='products-get-by-id'),
    path('products/<int:pk>/delete/', products_views.products_delete_by_id, name='products-delete-by-id'),
    path('products/delete/', products_views.products_delete_all, name='products-delete-all'),
    
    # Orders
    path('orders/', orders_views.order_list, name='order-list'),
    path('orders/<int:pk>/', orders_views.order_get_by_id, name='order-get-by-id'),
    path('orders/<int:pk>/delete/', orders_views.order_delete_by_id, name='order-delete-by-id'),
    path('orders/delete/', orders_views.order_delete_all, name='order-delete-all'),

    # Order Items
    path('orderItems/', orderItems_views.orderItems_list, name='orderItems-list'),
    path('orderItems/<int:pk>/', orderItems_views.orderItems_get_by_id, name='orderItems-get-by-id'),
    path('orderItems/<int:pk>/delete/', orderItems_views.orderItems_delete_by_id, name='orderItems-delete-by-id'),
    path('orderItems/delete/', orderItems_views.orderItems_delete_all, name='orderItems-delete-all'),

    # Carts
    path('carts/', carts_views.carts_list, name='carts-list'),
    path('carts/<int:pk>/', carts_views.carts_get_by_id, name='carts-get-by-id'),
    path('carts/<int:pk>/delete/', carts_views.carts_delete_by_id, name='carts-delete-by-id'),
    path('carts/delete/', carts_views.carts_delete_all, name='carts-delete-all'),

    # Cart Items
    path('cartItems/', cartItems_views.cartItems_list, name='cartItems-list'),
    path('cartItems/<int:pk>/', cartItems_views.cartItems_get_by_id, name='cartItems-get-by-id'),
    path('cartItems/<int:pk>/delete/', cartItems_views.cartItems_delete_by_id, name='cartItems-delete-by-id'),
    path('cartItems/delete/', cartItems_views.cartItems_delete_all, name='cartItems-delete-all'),
]