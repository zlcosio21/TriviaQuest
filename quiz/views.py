from django.shortcuts import render, redirect
from quiz.models import Quiz, CategoriaQuiz
from validators import correct_option

# Create your views here.
def creacion_quiz(request):
    if request.method ==  "POST":
        categoria = request.POST.get("categoria")
        pregunta = request.POST.get("pregunta")
        primera_opcion = request.POST.get("primera_opcion")
        segunda_opcion = request.POST.get("segunda_opcion")
        tercera_opcion = request.POST.get("tercera_opcion")
        cuarta_opcion = request.POST.get("cuarta_opcion")
        opcion_correcta = request.POST.get("opcion_correcta")

        categoria_fk, created = CategoriaQuiz.objects.get_or_create(nombre=categoria)
        opcion_correcta = correct_option(primera_opcion, segunda_opcion, tercera_opcion, cuarta_opcion, opcion_correcta)

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

    context = {
        "respuestas_correctas":respuestas_correctas,
        "quiz":quiz,
        "pregunta_actual":pregunta_actual,
        "num_preguntas":num_preguntas,
        "categoria":categoria, "tiempo":tiempo
    }

    return render(request, "quiz/juego_quiz.html", context)