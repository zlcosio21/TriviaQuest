from django.contrib import admin
from django.urls import path
from quiz import views

urlpatterns = [
    path('creacion_quiz/', views.creacion_quiz, name="creacion_quiz"),
    path('eleccion_quizes/', views.eleccion_quizes, name="eleccion_quizes"),
]
