from django.urls import path, include
from user_profile import views

urlpatterns = [

    path('', views.profile, name="perfil"),
    path('ranking/', views.ranking, name="ranking"),

]
