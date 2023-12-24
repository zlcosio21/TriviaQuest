from django.contrib import admin
from django.urls import path
from quiz import views

urlpatterns = [
    path('creacion_quiz/', views.creacion_quiz, name="creacion_quiz"),
    path('prueba_creacion_quiz/', views.prueba_creacion_quiz, name="prueba_creacion_quiz"),
]
