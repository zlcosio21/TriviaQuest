from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include("TriviaQuestApp.urls")),
    path('quiz/', include("quiz.urls")),
    path('autenticacion/', include("autenticacion.urls")),

]
