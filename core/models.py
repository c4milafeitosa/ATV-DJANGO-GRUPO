from django.db import models
from django.contrib.auth.models import User

class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.user.username

class Professor(models.Model):
    nome = models.CharField(max_length=50)
    especialidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    professores = models.ManyToManyField(Professor)

    def __str__(self):
        return self.nome

class Turma(models.Model):
    nome = models.CharField(max_length=50)
    disciplinas = models.ManyToManyField(Disciplina)
    professores = models.ManyToManyField(Professor)
    alunos = models.ManyToManyField(Aluno, related_name='turmas')

    def __str__(self):
        return self.nome

class Notas(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.aluno.user.username} - {self.turma.nome} - {self.nota}"

class Frequencia(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    presente = models.BooleanField()

    def __str__(self):
        return f"{self.aluno.user.username} - {self.turma.nome} - {'Presente' if self.presente else 'Ausente'}"
