from django.db import models
from django.contrib.auth.models import User
from TriviaQuest.base_models import Models

# Create your models here.

class CategoriaQuiz(Models):
    nombre = models.CharField(max_length=30, unique=True, null=False)

    def __str__(self):
        return self.nombre

class Quiz(Models):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(CategoriaQuiz, on_delete=models.CASCADE)
    pregunta = models.CharField(max_length=100, unique=100, null=False)
    primera_opcion = models.CharField(max_length=90, null=False)
    segunda_opcion = models.CharField(max_length=90, null=False)
    tercera_opcion = models.CharField(max_length=90, null=False)
    cuarta_opcion = models.CharField(max_length=90, null=False)
    opcion_correcta = models.CharField(max_length=90, null=False)

    def __str__(self):
        return f"Usuario {self.usuario.username} - Categoria {self.categoria.nombre} - Pregunta {self.pregunta} - Correcta {self.opcion_correcta}"