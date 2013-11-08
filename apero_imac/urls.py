from django.conf.urls import patterns, include, url

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
)
