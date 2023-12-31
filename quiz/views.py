from django.shortcuts import render, redirect
from quiz.models import Quiz, CategoriaQuiz
from validators import correct_option
from django.contrib import messages
import random

# Create your views here.
def creacion_quiz(request):
    if request.method ==  "POST":

        if not request.user.is_authenticated:
            messages.error(request, "Para poder crear quizes, debe iniciar sesion", extra_tags="create_quiz_login")
            return redirect("inicio_sesion")

        categoria = request.POST.get("categoria")
        pregunta = request.POST.get("pregunta")
        primera_opcion = request.POST.get("primera_opcion")
        segunda_opcion = request.POST.get("segunda_opcion")
        tercera_opcion = request.POST.get("tercera_opcion")
        cuarta_opcion = request.POST.get("cuarta_opcion")
        opcion_correcta = request.POST.get("opcion_correcta")

        categoria_fk, created = CategoriaQuiz.objects.get_or_create(nombre=categoria)
        opcion_correcta = correct_option(primera_opcion, segunda_opcion, tercera_opcion, cuarta_opcion, opcion_correcta)

        if Quiz.objects.filter(pregunta=pregunta).exists():
            messages.error(request, "La pregunta ya existe ingrese otra pregunta", extra_tags="quiz_exist")
            return redirect("creacion_quiz")

        Quiz.objects.create(
            usuario=request.user,
            categoria=categoria_fk,
            pregunta=pregunta,
            primera_opcion=primera_opcion,
            segunda_opcion=segunda_opcion,
            tercera_opcion=tercera_opcion,
            cuarta_opcion=cuarta_opcion,
            opcion_correcta=opcion_correcta,
        )

        return redirect("inicio")

    return render(request, "quiz/creacion_quiz.html")

def eleccion_quizes(request):
    categorias = CategoriaQuiz.objects.all()

    if request.method == "POST":
        num_preguntas = request.POST.get("num_preguntas")
        categoria = request.POST.get("categoria")
        tiempo = request.POST.get("tiempo")
        pregunta_actual = 1
        respuestas_correctas = 0

        return redirect("juego_quiz", respuestas_correctas, pregunta_actual, num_preguntas, categoria, tiempo)

    return render(request, "quiz/eleccion_quizes.html", {"categorias":categorias})

def juego_quiz(request, respuestas_correctas, pregunta_actual, num_preguntas, categoria, tiempo):
    categoria = CategoriaQuiz.objects.get(nombre=categoria)
    quiz = Quiz.objects.filter(categoria=categoria).order_by('?').first()

    if not quiz:
        messages.error(request, f"Actualmente no hay quizes para la categoria {categoria.nombre}", extra_tags="not_quizes_category")
        return redirect("eleccion_quizes")

    opciones_aleatorias = [quiz.primera_opcion, quiz.segunda_opcion, quiz.tercera_opcion, quiz.cuarta_opcion]
    random.shuffle(opciones_aleatorias)

    context = {
        "respuestas_correctas":respuestas_correctas,
        "quiz":quiz,
        "opciones":opciones_aleatorias,
        "pregunta_actual":pregunta_actual,
        "num_preguntas":num_preguntas,
        "categoria":categoria, "tiempo":tiempo
    }

    return render(request, "quiz/juego_quiz.html", context)

def comprobar_respuesta(request, pregunta, respuestas_correctas, pregunta_actual, num_preguntas, categoria, tiempo):
    if request.method == "POST":
        opcion_escogida = request.POST.get("opcion_escogida")

        quiz = Quiz.objects.get(pregunta=pregunta)
        respuestas_correctas +=  1 if opcion_escogida == quiz.opcion_correcta else 0
        pregunta_actual += 1

        if pregunta_actual > num_preguntas:
            return redirect("fin_juego_quiz", respuestas_correctas, num_preguntas)

        return redirect("juego_quiz", respuestas_correctas, pregunta_actual, num_preguntas, categoria, tiempo)

    return render(request, "quiz/juego_quiz.html")

def fin_juego_quiz(request, respuestas_correctas, num_preguntas):

    context = {
        "respuestas_correctas":respuestas_correctas,
        "num_preguntas":num_preguntas
    }

    return render(request, "quiz/fin_juego_quiz.html", context)