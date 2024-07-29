from django.urls import path, include
from django.contrib import admin

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('quiz/', include("quiz.urls")),
    path('autenticacion/', include("autenticacion.urls")),
    path('perfil/', include("user_profile.urls")),

]
