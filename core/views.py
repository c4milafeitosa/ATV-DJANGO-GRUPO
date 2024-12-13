from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Aluno, Professor, Disciplina, Turma, Notas, Frequencia
from .forms import AlunoForm, ProfessorForm, DisciplinaForm, TurmaForm, NotasForm, FrequenciaForm

# Página inicial
def index(request):
    return render(request, 'core/base.html')

# Alunos
@login_required
def aluno_list(request):
    alunos = Aluno.objects.all()
    return render(request, 'core/aluno_list.html', {'alunos': alunos})

@login_required
def aluno_create(request):
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('aluno_list')
    return render(request, 'core/aluno_form.html', {'form': form})

@login_required
def aluno_update(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    form = AlunoForm(request.POST or None, instance=aluno)
    if form.is_valid():
        form.save()
        return redirect('aluno_list')
    return render(request, 'core/aluno_form.html', {'form': form})

@login_required
def aluno_delete(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        aluno.delete()
        return redirect('aluno_list')
    return render(request, 'core/aluno_confirm_delete.html', {'aluno': aluno})

# Professores
@login_required
def professor_list(request):
    professores = Professor.objects.all()
    return render(request, 'core/professor_list.html', {'professores': professores})

@login_required
def professor_create(request):
    form = ProfessorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('professor_list')
    return render(request, 'core/professor_form.html', {'form': form})

@login_required
def professor_update(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    form = ProfessorForm(request.POST or None, instance=professor)
    if form.is_valid():
        form.save()
        return redirect('professor_list')
    return render(request, 'core/professor_form.html', {'form': form})

@login_required
def professor_delete(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    if request.method == 'POST':
        professor.delete()
        return redirect('professor_list')
    return render(request, 'core/professor_confirm_delete.html', {'professor': professor})

# Disciplinas
@login_required
def disciplina_list(request):
    disciplinas = Disciplina.objects.all()
    return render(request, 'core/disciplina_list.html', {'disciplinas': disciplinas})

@login_required
def disciplina_create(request):
    form = DisciplinaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('disciplina_list')
    return render(request, 'core/disciplina_form.html', {'form': form})

@login_required
def disciplina_update(request, pk):
    disciplina = get_object_or_404(Disciplina, pk=pk)
    form = DisciplinaForm(request.POST or None, instance=disciplina)
    if form.is_valid():
        form.save()
        return redirect('disciplina_list')
    return render(request, 'core/disciplina_form.html', {'form': form})

@login_required
def disciplina_delete(request, pk):
    disciplina = get_object_or_404(Disciplina, pk=pk)
    if request.method == 'POST':
        disciplina.delete()
        return redirect('disciplina_list')
    return render(request, 'core/disciplina_confirm_delete.html', {'disciplina': disciplina})

# Turmas
@login_required
def turma_list(request):
    turmas = Turma.objects.all()
    return render(request, 'core/turma_lista.html', {'turmas': turmas})

@login_required
def turma_create(request):
    form = TurmaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('turma_list')
    return render(request, 'core/turma_form.html', {'form': form})

@login_required
def turma_update(request, pk):
    turma = get_object_or_404(Turma, pk=pk)
    form = TurmaForm(request.POST or None, instance=turma)
    if form.is_valid():
        form.save()
        return redirect('turma_list')
    return render(request, 'core/turma_form.html', {'form': form})

@login_required
def turma_delete(request, pk):
    turma = get_object_or_404(Turma, pk=pk)
    if request.method == 'POST':
        turma.delete()
        return redirect('turma_list')
    return render(request, 'core/turma_confirm_delete.html', {'turma': turma})

# Notas
@login_required
def nota_list(request):
    notas = Notas.objects.all()
    return render(request, 'core/notas_list.html', {'notas': notas})

@login_required
def nota_create(request):
    form = NotasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('nota_list')
    return render(request, 'core/nota_form.html', {'form': form})

# Frequências
@login_required
def frequencia_list(request):
    frequencias = Frequencia.objects.all()
    return render(request, 'core/frequencia_list.html', {'frequencias': frequencias})

@login_required
def frequencia_create(request):
    form = FrequenciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('frequencia_list')
    return render(request, 'core/frequencia_form.html', {'form': form})
