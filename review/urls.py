from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from review.views import *


urlpatterns = patterns('review.views',
	url(r'(?P<pk>\d+)$', DetailReview.as_view(), name='review'),
	url(r'^$', ListView.as_view(model=Review, context_object_name="object_list", template_name="review_list.html")),
)
