from django.conf.urls import patterns, include, url
from consumer.views import *

urlpatterns = patterns('consumer.views',
	url(r'^$', 'profil'),
)