from quiz.models import CategoriaQuiz, Quiz
from django.shortcuts import render

def inicio(request):
    quizes = Quiz.random_quizes()
    categorias = CategoriaQuiz.random_categories()

    return render(request, "TriviaQuestApp/inicio.html", {"quizes":quizes, "categorias":categorias})