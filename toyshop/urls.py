from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from shop.views import hello

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'toyshop.views.home', name='home'),
                       # url(r'^toyshop/', include('toyshop.foo.urls')),

                       url(r'^$', hello, name='hello_message'),
                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
)
