from django import forms
from .models import Aluno, Professor, Disciplina, Turma, Notas, Frequencia

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['user', 'matricula']

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'especialidade']

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome', 'codigo', 'professores']

class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['nome', 'disciplinas', 'professores', 'alunos']
        widgets = {
            'alunos': forms.CheckboxSelectMultiple,
        }

class NotasForm(forms.ModelForm):
    class Meta:
        model = Notas
        fields = ['aluno', 'turma', 'nota']

class FrequenciaForm(forms.ModelForm):
    class Meta:
        model = Frequencia
        fields = ['aluno', 'turma', 'presente']
