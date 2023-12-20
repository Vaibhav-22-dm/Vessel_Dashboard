from django.urls import path
from .views import *

urlpatterns = [
    path('add_notification/', add_notification, name='add_notification'),
]