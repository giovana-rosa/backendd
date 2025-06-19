from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator

class Matricula(models.Model):
    nome = models.CharField(max_length=50)
   

    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=50)
    data_de_nascimento = models.DateField()
    formacao = models.CharField(max_length=50, verbose_name='Formação')
    matricula = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Frequencia(models.Model):
    nome = models.CharField(max_length=50)
   

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    CPF = models.CharField(max_length=11)
    data_de_nascimento = models.DateField()
    telefone = PhoneNumberField()
    email = models.CharField(max_length=50)
   

    def __str__(self):
        return self.nome


class Turma(models.Model):
    email_da_turma = models.CharField(max_length=50)


    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length=50)
    carga_horaria = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Carga Horária')
    ementa = models.TextField()
    programacao = models.TextField(verbose_name='Programação')
    avaliacao = models.DecimalField(max_digits=4, decimal_places=2, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], verbose_name='Avaliação')
   

    def __str__(self):
        return self.nome


class Curso(models.Model):
    nome = models.CharField(max_length=50)  
    ementa = models.TextField()  
    carga_horaria = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Carga Horária') 
    coordenador = models.CharField(max_length=50)  
    email = models.EmailField(max_length=50)  

    def __str__(self):
        return self.nome