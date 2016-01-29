from django.shortcuts import render
from .models import Consulta, Consultorio
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
# Create your views here.

def enviar_emails(request):
	consultas = Consulta.objects.all()
	for consulta in consultas:
		if not consulta.enviado and ( ( timezone.now() + timedelta(hours=24) ) > consulta.hora ):
			mensagem = consulta.nome + ", "
			mensagem += " sua consulta esta marcada para " + consulta.hora.strftime('o dia %d/%m as %H:%M:%S')
			mensagem += ", no consultorio " + consulta.consultorio.nome
			#mensagem += ". Confirme sua presenca"
			print mensagem + " PARA: " + consulta.email
			print "Settings: " + settings.EMAIL_HOST_USER
			send_mail('Consulta', mensagem, settings.EMAIL_HOST_USER, [consulta.email], fail_silently=False)
			consulta.enviado = True
			consulta.save()
			print consulta.hora
			print timezone.now()
			print timezone.now() + timedelta(hours=24)
			print ( ( timezone.now() + timedelta(hours=24) ) > consulta.hora )
	return HttpResponse("Emails enviados com sucesso.")