from django.db import models
from django.contrib.auth.models import User
from TriviaQuest.base_models import Models

# Create your models here.

class CategoriaQuiz(Models):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Quiz(Models):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(CategoriaQuiz, on_delete=models.CASCADE)
    pregunta = models.CharField(max_length=100)
    primera_opcion = models.CharField(max_length=90)
    segunda_opcion = models.CharField(max_length=90)
    tercera_opcion = models.CharField(max_length=90)
    cuarta_opcion = models.CharField(max_length=90)
    opcion_correcta = models.CharField(max_length=90)

    def __str__(self):
        return f"Usuario {self.usuario.username} - Categoria {self.categoria.nombre} - Pregunta {self.pregunta} - Correcta {self.opcion_correcta}"