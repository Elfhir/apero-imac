from consumer.models import *
from django.shortcuts import render_to_response
from datetime import datetime

def profil(request):
	consumer_list = Consumer.objects.all()
	
	return render_to_response('profil.html', locals())

def connexion(request):
	
	return render_to_response('connexion.html', locals())

def edit_profil(request):
	consumer_list = Consumer.objects.all()
	
	return render_to_response('edit_profil.html', locals())

def delete_profil(request):
	consumer_list = Consumer.objects.all()
	
	return render_to_response('delete_profil.html', locals())

def profil_list(request):
	consumer_list = Consumer.objects.all()
	
	return render_to_response('profil_list.html', locals())



