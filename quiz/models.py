from django.contrib.auth.models import User
from TriviaQuest.base_models import Models
from django.db import models
from random import sample
import random


# Create your models here.
class CategoriaQuiz(Models):
    nombre = models.CharField(max_length=30, unique=True, null=False)

    @classmethod
    def get_or_create(cls, nombre_categoria):
        categoria_quiz, created = cls.objects.get_or_create(nombre=nombre_categoria)

        return categoria_quiz

    @classmethod
    def random_categories(cls):
        return sample(list(CategoriaQuiz.objects.all()), min(4, CategoriaQuiz.objects.count()))

    def __str__(self):
        return self.nombre


class Quiz(Models):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(CategoriaQuiz, on_delete=models.CASCADE)
    pregunta = models.CharField(max_length=100, unique=True, null=False)
    primera_opcion = models.CharField(max_length=90, null=False)
    segunda_opcion = models.CharField(max_length=90, null=False)
    tercera_opcion = models.CharField(max_length=90, null=False)
    cuarta_opcion = models.CharField(max_length=90, null=False)
    opcion_correcta = models.CharField(max_length=90, null=False)

    @classmethod
    def create(cls, request, categoria, pregunta, primera_opcion, segunda_opcion, tercera_opcion, cuarta_opcion, opcion_correcta):
        return cls.objects.create(
            usuario=request.user,
            categoria=categoria,
            pregunta=pregunta,
            primera_opcion=primera_opcion,
            segunda_opcion=segunda_opcion,
            tercera_opcion=tercera_opcion,
            cuarta_opcion=cuarta_opcion,
            opcion_correcta=opcion_correcta,
        )

    def correct_answers(self, opcion_escogida):
        return 1 if self.opcion_correcta ==  opcion_escogida else 0

    @staticmethod
    def correct_option(primera_opcion, segunda_opcion, tercera_opcion, cuarta_opcion, opcion_correcta):

        OPCIONES = {
            'A': primera_opcion,
            'B': segunda_opcion,
            'C': tercera_opcion,
            'D': cuarta_opcion,
        }

        return OPCIONES.get(opcion_correcta)

    @classmethod
    def already_exist(cls, pregunta):
        return cls.objects.filter(pregunta=pregunta).exists()

    @classmethod
    def not_sufficient_quizes(cls, categoria, num_preguntas):
        categoria_obj = CategoriaQuiz.objects.get(nombre=categoria)

        return cls.objects.filter(categoria=categoria_obj).count() < int(num_preguntas)

    @classmethod
    def random_quiz(cls, categoria):
        return cls.objects.filter(categoria=categoria).order_by('?').first()

    @classmethod
    def random_quizes(cls):
        return sample(list(cls.objects.all()), min(6, cls.objects.count()))

    def random_options(self):
        random_options = [self.primera_opcion, self.segunda_opcion, self.tercera_opcion, self.cuarta_opcion]
        random.shuffle(random_options)

        return random_options

    def __str__(self):
        return f"Usuario {self.usuario.username} - Categoria {self.categoria.nombre} - Pregunta {self.pregunta} - Correcta {self.opcion_correcta}"