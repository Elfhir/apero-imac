from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from product.views import *


urlpatterns = patterns('product.views',
	url(r'(?P<pk>\d+)$', DetailDrink.as_view(), name='Drink'),
	url(r'^$', ListView.as_view(model=Drink, context_object_name="object_list", template_name="product_list.html")),
	url(r'^list/$', ListView.as_view(model=Drink, context_object_name="object_list", template_name="product_list.html")),
)
