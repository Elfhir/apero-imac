from review.models import *
from django.shortcuts import render_to_response
from datetime import datetime


def display_first_page(request):
	reviews = Review.objects.all();
	
	return render_to_response('review_list.html', locals())

def display_other_page(request, page):
	reviews = Review.objects.all();
	
	return render_to_response('review_list.html', locals())

def display_item_by_name(request, name):
	
	return render_to_response('review.html', locals())

