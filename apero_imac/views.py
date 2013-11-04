from apero_imac.models import *
from django.shortcuts import render_to_response
from datetime import datetime

def index(request):
	
	return render_to_response('common/index.html', locals())

def about(request):

	return render_to_response('common/about.html', locals())
