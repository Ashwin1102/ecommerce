from django.contrib import admin
from django.urls import path
from customers import views as customer_views
from geolocations import views as geolocations_views
from sellers import views as sellers_views
from django.shortcuts import redirect

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

    # Geolocations
    path('geolocations/', geolocations_views.geolocation_list, name='geolocation-list'),
    path('geolocations/<int:pk>/', geolocations_views.geolocation_get_by_id, name='geolocation-get-by-id'),
    path('geolocations/<int:pk>/delete/', geolocations_views.geolocation_delete_by_id, name='geolocation-delete-by-id'),
    path('geolocations/delete/', geolocations_views.geolocation_delete_all, name='geolocation-delete-all'),

    # Sellers
    path('sellers/', sellers_views.sellers_list, name='seller-list'),
]
