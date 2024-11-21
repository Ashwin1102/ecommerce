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
    path('customers/', customer_views.customer_list, name='customer-list'),
    path('geolocations/', geolocations_views.geolocation_list, name='geolocation-list'),
    path('sellers/', sellers_views.sellers_list, name='seller-list')
]
