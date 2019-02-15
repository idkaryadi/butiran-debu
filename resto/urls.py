from django.urls import path
from . import views

urlpatterns = [
    path('', views.detail_resto, name = 'restorant'),
    path('/menu', views.detail_menu, name = 'menu'),
    path('/reservasi', views.detail_resev, name = 'reservasi'),
]