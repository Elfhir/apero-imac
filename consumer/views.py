from consumer.models import *
from django.shortcuts import render_to_response
from datetime import datetime

def profil(request):
	consumer_list = Consumer.objects.all()
	
	return render_to_response('consumer/profil.html', locals())

def connexion(request):
	
	return render_to_response('consumer/connexion.html', locals())

def edit_profil(request):
	consumer_list = Consumer.objects.all()
	
	return render_to_response('consumer/edit_profil.html', locals())

def delete_profil(request):
	consumer_list = Consumer.objects.all()
	
	return render_to_response('consumer/delete_profil.html', locals())

def profil_list(request):
	consumer_list = Consumer.objects.all()
	
	return render_to_response('consumer/profil_list.html', locals())



