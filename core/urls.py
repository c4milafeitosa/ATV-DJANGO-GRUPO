from django.urls import path
from . import views

urlpatterns = [
    # Página inicial
    path('', views.index, name='index'),

    # Alunos
    path('alunos/', views.aluno_list, name='aluno_list'),
    path('alunos/new/', views.aluno_create, name='aluno_create'),
    path('alunos/edit/<int:pk>/', views.aluno_update, name='aluno_update'),
    path('alunos/delete/<int:pk>/', views.aluno_delete, name='aluno_delete'),

    # Professores
    path('professores/', views.professor_list, name='professor_list'),
    path('professores/new/', views.professor_create, name='professor_create'),
    path('professores/edit/<int:pk>/', views.professor_update, name='professor_update'),
    path('professores/delete/<int:pk>/', views.professor_delete, name='professor_delete'),

    # Disciplinas
    path('disciplinas/', views.disciplina_list, name='disciplina_list'),
    path('disciplinas/new/', views.disciplina_create, name='disciplina_create'),
    path('disciplinas/edit/<int:pk>/', views.disciplina_update, name='disciplina_update'),
    path('disciplinas/delete/<int:pk>/', views.disciplina_delete, name='disciplina_delete'),

    # Turmas
    path('turmas/', views.turma_list, name='turma_list'),
    path('turmas/new/', views.turma_create, name='turma_create'),
    path('turmas/edit/<int:pk>/', views.turma_update, name='turma_update'),
    path('turmas/delete/<int:pk>/', views.turma_delete, name='turma_delete'),

    # Notas
    path('notas/', views.nota_list, name='nota_list'),
    path('notas/new/', views.nota_create, name='nota_create'),

    # Frequências
    path('frequencias/', views.frequencia_list, name='frequencia_list'),
    path('frequencias/new/', views.frequencia_create, name='frequencia_create'),
]
