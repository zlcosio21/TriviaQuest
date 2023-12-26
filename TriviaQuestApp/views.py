from django.shortcuts import render
from quiz.models import CategoriaQuiz, Quiz
from random import sample

def inicio(request):
    categorias = sample(list(CategoriaQuiz.objects.all()), min(4, CategoriaQuiz.objects.count()))
    quizes = sample(list(Quiz.objects.all()), min(6, Quiz.objects.count()))

    return render(request, "TriviaQuestApp/inicio.html", {"quizes":quizes, "categorias":categorias})