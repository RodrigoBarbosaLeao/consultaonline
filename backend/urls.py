from django.conf.urls import patterns, url
from backend import views

urlpatterns = [
	url(r'^enviar_emails', views.enviar_emails, name='enviar_emails')
]