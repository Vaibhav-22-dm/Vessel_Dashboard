from django.urls import path
from .views import *

urlpatterns = [
    path('create_port/', create_port, name='create_port'),
    path('create_vessel/', create_vessel, name='create_vessel'),
    path('get_port/<str:pk>/', get_port, name='get_port'),
    path('get_ports/', get_ports, name='get_ports'),
    path('get_vessel/<str:pk>/', get_vessel, name='get_vessel'),
    path('get_vessels/', get_vessels, name='get_vessels'),
    path('get_port_vessels/<str:pk>/', get_port_vessels, name='get_port_vessels'),
]