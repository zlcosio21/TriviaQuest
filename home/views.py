from quiz.models import CategoriaQuiz, Quiz
from django.shortcuts import render


def home(request):
    return render(request, "home/home.html")