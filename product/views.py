from product.models import *
from django.shortcuts import render_to_response
from datetime import datetime

# Create your views here.
def display(request):
	
	return render_to_response('product/product.html', locals())