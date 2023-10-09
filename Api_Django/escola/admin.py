from django.contrib import admin
from escola.models import Aluno, Curso

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'rg', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'cpf', 'rg', 'data_nascimento', 'id')
    list_per_page = 20

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao', 'nivel')
    list_display_links = ('id', 'codigo_curso', 'descricao')
    search_fields = ('codigo_curso', 'descricao', 'nivel', 'id')
    list_per_page = 20

admin.site.register(Aluno, Alunos)
admin.site.register(Curso, Cursos)