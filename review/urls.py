from django.conf.urls import patterns, include, url
from review.views import *


urlpatterns = patterns('review.views',
	url(r'^$', 'display'),
)
