from consumer.models import *
from django.shortcuts import render_to_response
from datetime import datetime

def profil(request):
	
	return render_to_response('consumer/profil.html', locals())

