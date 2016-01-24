from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here.
class Consultorio(models.Model):
	nome = models.CharField(max_length=30)
	senha = models.CharField(max_length=30)

class Consulta(models.Model):
	telefone = models.CharField(max_length=20, null=False)
	mensagem = models.CharField(max_length=255, null=False)
	hora = models.DateTimeField(null=False)
	confirmado = models.BooleanField(default=False, null=False)
	consultorio = models.ForeignKey(Consultorio, related_name='consultas')
