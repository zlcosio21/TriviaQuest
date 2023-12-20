from django.db import models
from django.contrib.auth.models import User
from TriviaQuest.base_models import Models

# Create your models here.

class CategoriaQuiz(Models):
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return f"Categoria {self.nombre}"

class Quiz(Models):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(CategoriaQuiz, on_delete=models.CASCADE)
    pregunta = models.CharField(max_length=100)
    primera_opcion = models.CharField(max_length=100)
    segunda_opcion = models.CharField(max_length=100)
    tercera_opcion = models.CharField(max_length=100)
    cuarta_opcion = models.CharField(max_length=100)

    OPCIONES = [
        ('primera_opcion', 'Primera Opción'),
        ('segunda_opcion', 'Segunda Opción'),
        ('tercera_opcion', 'Tercera Opción'),
        ('cuarta_opcion', 'Cuarta Opción'),
    ]

    opcion_correcta = models.CharField(max_length=100, choices=OPCIONES, default='primera_opcion')

    def __str__(self):
        return f"Usuario {self.usuario.username} - Categoria {self.categoria.nombre} - Pregunta {self.pregunta}"