from django.conf.urls import patterns, include, url
from consumer.views import *

urlpatterns = patterns('consumer.views',
	url(r'^$', 'profil'),
	url(r'^profil/$', 'profil'),
	url(r'^connexion/$', 'connexion'),
	url(r'^edit/$', 'edit_profil'),
	url(r'^delete/$', 'delete_profil'),
	url(r'^list/$', 'profil_list'),
)