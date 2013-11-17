from review.models import *
from django.shortcuts import render_to_response
from django.views.generic import ListView, DetailView
from datetime import datetime


class ListReview(ListView):
	model = Review
	context_object_name = "review_list"
	template_name = "review_list.html"
	paginate_by = 5


class DetailReview(DetailView):
	model = Review
	context_object_name = "review"
	template_name = "review.html"