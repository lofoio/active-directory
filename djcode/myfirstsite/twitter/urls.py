from django.conf.urls.defaults import *
from myfirstsite.twitter.views import public


urlpatterns = patterns('',
    (r'^$', public),
)
