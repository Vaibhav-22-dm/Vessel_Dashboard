from django.urls import path
from .views import *

urlpatterns = [
    path('predict_trajectory/', predict_trajectory, name='predict_trajectory'),
    path('predict_fuel_consumption/', predict_fuel_consumption, name='predict_fuel_consumption'),
]