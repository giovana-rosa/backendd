from django.db import models

class Matricula(models.Model):
    nome = models.CharField(max_length=50)
   

    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=50)
   

    def __str__(self):
        return self.nome
