from django.shortcuts import render
from quiz.models import Quiz

# Create your views here.
def perfil(request):

    return  render(request, "perfil/perfil.html")

def editar_perfil(request):

    return render(request, "perfil/editar_perfil.html")