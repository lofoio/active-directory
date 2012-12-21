from django.conf.urls.defaults import *
from django.conf import settings
from myfirstsite.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
        (r'^comments/', include('django.contrib.comments.urls')),
        (r'^blog/', include('blog.urls')),
        (r'^contact/', include('contact.urls')),
        (r'^admin/', include(admin.site.urls)),
        (r'^admin/doc/', include('django.contrib.admindocs.urls')),
        (r'^twitter/', include('twitter.urls')),
        (r'^poll/', include('poll.urls')),
        url(r'^homepage/$', display_meta, name="home_page" ),
        (r'^time/$', current_datetime),
        (r'^time/plus/(\d{1,2})/$', hours_ahead),
        url(r'^$', home_page),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^debuginfo/$', debug),
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )

urlpatterns += patterns('',
    url(r'^(?P<template>\w+)/$', static_page, name="static_page"),
)
