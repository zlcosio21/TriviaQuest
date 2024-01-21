from django.contrib import admin
from django.urls import path
from perfil import views

urlpatterns = [
    path('', views.perfil, name="perfil"),
    path('editar_perfil/', views.editar_perfil, name="editar_perfil")
]
