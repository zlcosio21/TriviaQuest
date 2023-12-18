from django.contrib import admin
from django.urls import path
from TriviaQuestApp import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
]
