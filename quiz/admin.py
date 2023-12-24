from django.contrib import admin
from quiz.models import CategoriaQuiz, Quiz

# Register your models here.
class CategoriaQuizAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class QuizAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(CategoriaQuiz, CategoriaQuizAdmin)
admin.site.register(Quiz, QuizAdmin)