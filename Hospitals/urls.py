from django.urls import path
from . import views

urlpatterns = [
    path('', views.Hospital_list, name='Hospital_list'),
]