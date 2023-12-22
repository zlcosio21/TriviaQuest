from django.shortcuts import render, redirect
from preguntas.models import Quiz, CategoriaQuiz
from preguntas.forms import CreacionQuiz

# Create your views here.
def preguntas(request):
    creacion_quiz = CreacionQuiz()

    if request.method ==  "POST":
        categoria = request.POST.get("categoria")
        pregunta = request.POST.get("pregunta")
        primera_opcion = request.POST.get("primera_opcion")
        segunda_opcion = request.POST.get("segunda_opcion")
        tercera_opcion = request.POST.get("tercera_opcion")
        cuarta_opcion = request.POST.get("cuarta_opcion")
        opcion_correcta = request.POST.get("opcion_correcta")

        categoria_fk, created = CategoriaQuiz.objects.get_or_create(nombre__iexact=categoria)

        OPCIONES = {
            'primera_opcion': primera_opcion,
            'segunda_opcion': segunda_opcion,
            'tercera_opcion': tercera_opcion,
            'cuarta_opcion': cuarta_opcion,
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

        return redirect("prueba_creacion_quiz")

    return render(request, "preguntas/prueba.html", {"creacion_quiz":creacion_quiz})

def prueba_creacion_quiz(request):
    quizes = Quiz.objects.filter(usuario=request.user)

    return render(request, "preguntas/prueba_quiz.html", {"quizes":quizes})