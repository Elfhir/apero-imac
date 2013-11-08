from django.conf.urls import patterns, include, url
from review.views import *


urlpatterns = patterns('review.views',
	url(r'^$', 'display_first_page'),
	url(r'^list/', 'display_first_page'),
	url(r'^list/(?P<page>\d{3})', 'display_other_page'),
	url(r'^item/(?P<name>\w+)', 'display_item_by_name'),
)
