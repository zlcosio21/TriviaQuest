from django import forms

class CreacionQuiz(forms.Form):
    categoria = forms.CharField(label="Categoria", max_length=80)
    pregunta = forms.CharField(label="Pregunta", max_length=100)
    primera_opcion = forms.CharField(label="Primera Opcion", max_length=100)
    segunda_opcion = forms.CharField(label="Segunda Opcion", max_length=100)
    tercera_opcion = forms.CharField(label="Tercera Opcion", max_length=100)
    cuarta_opcion = forms.CharField(label="Cuarta Opcion", max_length=100)

    OPCIONES = [
        ('primera_opcion', 'Primera Opcion'),
        ('segunda_opcion', 'Segunda Opcion'),
        ('tercera_opcion', 'Tercera Opcion'),
        ('cuarta_opcion', 'Cuarta Opcion'),
    ]

    opcion_correcta = forms.ChoiceField(label="Opcion Correcta", choices=OPCIONES)