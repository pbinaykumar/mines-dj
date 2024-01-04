from django.urls import path
from . import views

urlpatterns = [
        path('vehicle_status', views.vehicle_status),
        path('vehicle_list', views.vehicle_list),
        path('vehicle_history', views.vehicle_history),
    ]