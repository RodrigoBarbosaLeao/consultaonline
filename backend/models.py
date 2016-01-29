from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here.
class Consultorio(models.Model):
	nome = models.CharField(max_length=30)
	senha = models.CharField(max_length=30)

	def __str__(self):
		return self.nome

class Consulta(models.Model):
	email = models.CharField(max_length=50, null=False)
	nome = models.CharField(max_length=50, null=False)
	hora = models.DateTimeField(null=False)
	#Se ja foi enviado
	enviado = models.BooleanField(default=False, null=False)
	#Se foi confirmado
	confirmado = models.BooleanField(default=False, null=False)
	consultorio = models.ForeignKey(Consultorio, related_name='consultas')
	
	def __str__(self):
		return self.nome
