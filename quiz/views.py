from django.shortcuts import render, redirect
from quiz.models import Quiz, CategoriaQuiz

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

        OPCIONES = {
            'A': primera_opcion,
            'B': segunda_opcion,
            'C': tercera_opcion,
            'D': cuarta_opcion,
        }

        opcion_correcta = OPCIONES.get(opcion_correcta)

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
        categoria = CategoriaQuiz.objects.get(nombre=categoria)
        tiempo = request.POST.get("tiempo")

        quiz = Quiz.objects.get(categoria=categoria)

        return render(request, "quiz/juego_quiz.html", {"quiz":quiz, "num_preguntas":num_preguntas, "categoria":categoria, "tiempo":tiempo})

    return render(request, "quiz/eleccion_quizes.html", {"categorias":categorias})

def juego_quiz(request):

    return render(request, "quiz/juego_quiz.html")