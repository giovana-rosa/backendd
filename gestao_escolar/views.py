from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Matricula
from .models import Professor
from .models import Aluno
from .models import Turma
from .models import Curso
from .models import Frequencia
from .models import Disciplina
from .serializers import MatriculaSerializer
from .serializers import ProfessorSerializer
from .serializers import AlunoSerializer
from .serializers import TurmaSerializer
from .serializers import CursoSerializer
from .serializers import FrequenciaSerializer
from .serializers import DisciplinaSerializer


class MatriculaViewSet(ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ProfessorViewSet(ModelViewSet):
    queryset = Professor.objects.all()  
    serializer_class = ProfessorSerializer

class AlunoViewSet(ModelViewSet):
    queryset = Aluno.objects.all() 
    serializer_class = AlunoSerializer

class TurmaViewSet(ModelViewSet):
    queryset = Turma.objects.all()  
    serializer_class = TurmaSerializer

class CursoViewSet(ModelViewSet):
    queryset = Curso.objects.all() 
    serializer_class = CursoSerializer

class FrequenciaViewSet(ModelViewSet):
    queryset = Frequencia.objects.all()  
    serializer_class = FrequenciaSerializer

class DisciplinaViewSet(ModelViewSet):
    queryset = Disciplina.objects.all()  
    serializer_class = DisciplinaSerializer