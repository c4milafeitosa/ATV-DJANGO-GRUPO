from django.contrib import admin
from .models import Aluno, Professor, Disciplina, Turma, Notas, Frequencia

admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Disciplina)
admin.site.register(Turma)
admin.site.register(Notas)
admin.site.register(Frequencia)
