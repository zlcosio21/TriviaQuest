from utils.validators import not_authenticated
from django.shortcuts import render, redirect
from quiz.models import Quiz, CategoriaQuiz
from django.contrib import messages


# Create your views here.
def creacion_quiz(request):
    if request.method ==  "POST":
        pregunta = request.POST.get("pregunta")

        if not_authenticated(request):
            messages.error(request, "Para poder crear quizes, debe iniciar sesion", extra_tags="create_quiz_login")
            return redirect("inicio_sesion")

        if Quiz.already_exist(pregunta):
            messages.error(request, "La pregunta ya existe ingrese otra pregunta", extra_tags="quiz_exist")
            return redirect("creacion_quiz")

        categoria = request.POST.get("categoria")
        primera_opcion = request.POST.get("primera_opcion")
        segunda_opcion = request.POST.get("segunda_opcion")
        tercera_opcion = request.POST.get("tercera_opcion")
        cuarta_opcion = request.POST.get("cuarta_opcion")
        opcion_correcta = request.POST.get("opcion_correcta")

        categoria = CategoriaQuiz.get_or_create(categoria)
        opcion_correcta = Quiz.correct_option(primera_opcion, segunda_opcion, tercera_opcion, cuarta_opcion, opcion_correcta)
        Quiz.create(request, categoria, pregunta, primera_opcion, segunda_opcion, tercera_opcion, cuarta_opcion, opcion_correcta)

        return redirect("eleccion_quizes")

    return render(request, "quiz/creacion_quiz.html")


def eleccion_quizes(request):
    categorias = CategoriaQuiz.objects.all()

    if request.method == "POST":
        categoria = request.POST.get("categoria")
        num_preguntas = request.POST.get("num_preguntas")

        if Quiz.not_sufficient_quizes(categoria, num_preguntas):
            messages.error(request, "Lo sentimos, no hay suficientes preguntas disponibles para poder continuar", extra_tags="not_sufficient_quizzes")
            return redirect("eleccion_quizes")

        request.session["tiempo"] = request.POST.get("tiempo")
        request.session["categoria"] = categoria
        request.session["num_preguntas"] = num_preguntas
        request.session["num_pregunta_actual"] = 1
        request.session["respuestas_correctas"] = 0

        return redirect("juego_quiz")

    return render(request, "quiz/eleccion_quizes.html", {"categorias":categorias})


def juego_quiz(request):
    tiempo = request.session.get("tiempo")
    categoria = request.session.get("categoria")
    num_preguntas = request.session.get("num_preguntas")
    num_pregunta_actual = request.session.get("num_pregunta_actual")
    respuestas_correctas = request.session.get("respuestas_correctas")

    categoria = CategoriaQuiz.objects.get(nombre=categoria)
    quiz = Quiz.random_quiz(categoria)

    request.session["pregunta"] = quiz.pregunta
    opciones_aleatorias = quiz.random_options()

    context = {
        "tiempo":tiempo,
        "categoria":categoria,
        "num_preguntas":num_preguntas,
        "num_pregunta_actual":num_pregunta_actual,
        "respuestas_correctas":respuestas_correctas,
        "opciones":opciones_aleatorias,
        "quiz": quiz
    }

    return render(request, "quiz/juego_quiz.html", context)


def comprobar_respuesta(request):
    if request.method == "POST":
        num_preguntas = request.session.get("num_preguntas")
        num_pregunta_actual = request.session.get("num_pregunta_actual")
        respuestas_correctas = request.session.get("respuestas_correctas")
        opcion_escogida = request.POST.get("opcion_escogida")

        pregunta = request.session.get("pregunta")
        quiz = Quiz.objects.get(pregunta=pregunta)

        respuestas_correctas += quiz.correct_answers(opcion_escogida)
        num_pregunta_actual += 1

        request.session["num_pregunta_actual"] = num_pregunta_actual
        request.session["respuestas_correctas"] = respuestas_correctas

        if num_pregunta_actual > int(num_preguntas):
            return redirect("fin_juego_quiz")

        return redirect("juego_quiz")

    return render(request, "quiz/juego_quiz.html")


def fin_juego_quiz(request):
    num_preguntas = request.session.get("num_preguntas")
    respuestas_correctas = request.session.get("respuestas_correctas")

    request.session.flush()

    return render(request, "quiz/fin_juego_quiz.html", {"respuestas_correctas":respuestas_correctas, "num_preguntas":num_preguntas})
