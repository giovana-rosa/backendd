from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator

class Matricula(models.Model):
    STATUS_CHOICES = [('ativa', 'Ativa'), ('trancada', 'Trancada'), ('cancelada', 'Cancelada'), ('concluida', 'Concluída')]
    modalidade_de_ensino = models.CharField(max_length=50)
    data_de_matricula = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    nota_final = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    observacoes = models.TextField(verbose_name='Observações')
    frequencia_final = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    aluno = models.ForeignKey('Aluno', on_delete=models.CASCADE)
    turma = models.ForeignKey('Turma', on_delete=models.CASCADE)

    def __str__(self):
        return f"Matricula de {self.aluno.nome} na turma {self.turma}"

class Professor(models.Model):
    nome = models.CharField(max_length=50)
    data_de_nascimento = models.DateField()
    formacao = models.CharField(max_length=50, verbose_name='Formação')
    matricula = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    CPF = models.CharField(max_length=11)
    data_de_nascimento = models.DateField()
    telefone = PhoneNumberField()
    email = models.EmailField(max_length=50)
   
    def __str__(self):
        return self.nome


class Turma(models.Model):
    email = models.EmailField(max_length=50)
    data_inicial = models.DateField()
    data_final = models.DateField()
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)

    def __str__(self):
        return f"Turma de {self.curso.nome} ({self.data_inicial} - {self.data_final})"


class Disciplina(models.Model):
    nome = models.CharField(max_length=50)
    carga_horaria = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Carga Horária')
    ementa = models.TextField()
    programacao = models.TextField(verbose_name='Programação')
    avaliacao = models.DecimalField(max_digits=4, decimal_places=2, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], verbose_name='Avaliação')
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)
    coordenador = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Frequencia(models.Model):
    data = models.DateField()
    presenca = models.BooleanField(verbose_name='Presença')
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

    def __str__(self):
        status = "Presente" if self.presenca else "Faltou"
        return f"{self.aluno.nome} - {status} em {self.data}"

class Curso(models.Model):
    nome = models.CharField(max_length=50)  
    ementa = models.TextField()  
    carga_horaria = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Carga Horária') 
    coordenador = models.ForeignKey('Professor', on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(max_length=50)  

    def __str__(self):
        return self.nome