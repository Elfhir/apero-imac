from django.conf.urls import patterns, include, url

# Require User Login for Databrowse
from django.contrib.auth.decorators import login_required

# Databrowse
from django.contrib import databrowse

# Classes for Databrowse
from consumer.models import Consumer
from product.models import Drink, Appetizer
from review.models import Review

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'apero_imac.views.home', name='home'),
	url(r'^about/$', 'apero_imac.views.about', name='about'),
	url(r'^consumer/', include('consumer.urls'), name="consumer"),
	url(r'^review/', include('review.urls'), name="review"),
	url(r'^product/', include('product.urls'), name="product"),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^databrowse/(.*)', databrowse.site.root),
	#url(r'^databrowse/(.*)', login_required(databrowse.site.root)),
)

# Register Classes for Databrowse
databrowse.site.register(Consumer, Appetizer, Drink, Review)


