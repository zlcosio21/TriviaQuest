from django.shortcuts import render
from quiz.models import CategoriaQuiz, Quiz

# Create your views here.
def inicio(request):
    categorias = CategoriaQuiz.objects.all()[:4]
    quizes = Quiz.objects.all()[:6]

    return render(request, "TriviaQuestApp/inicio.html", {"quizes":quizes, "categorias":categorias})