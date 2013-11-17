from product.models import *
from django.shortcuts import render_to_response
from django.views.generic import ListView, DetailView
from datetime import datetime


class ListDrink(ListView):
	model = Drink
	context_object_name = "product_list"
	template_name = "product_list.html"
	paginate_by = 5

class DetailDrink(DetailView):
	model = Drink
	context_object_name = "product"
	template_name = "product.html"

class ListAppetizer(ListView):
	model = Appetizer
	context_object_name = "product_list"
	template_name = "product_list.html"
	paginate_by = 5

class DetailAppetizer(DetailView):
	model = Appetizer
	context_object_name = "product"
	template_name = "product.html"