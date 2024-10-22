from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('developments/<int:development_id>/', development),
    path('services/<int:service_id>/', service),
]