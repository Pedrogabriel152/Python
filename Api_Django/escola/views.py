from escola.serializers import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosCursoSerializer
from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""    
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    
class CursoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as Matricula"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as Matriculos de um aluno"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer
    
class ListaAlunosCurco(generics.ListAPIView):
    """Listando os aluno de um curso"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosCursoSerializer