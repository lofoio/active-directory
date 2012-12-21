from django.conf.urls.defaults import *
from myfirstsite.contact.views import contact, thanks

urlpatterns = patterns('',
                url(r'^$', contact, name="contact" ),
                (r'^thanks/$', thanks),
)
