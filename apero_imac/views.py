from apero_imac.models import *
from django.shortcuts import render_to_response
from datetime import datetime

def home(request):
	
	return render_to_response('common/home.html', locals())

def about(request):

	return render_to_response('common/about.html', locals())
