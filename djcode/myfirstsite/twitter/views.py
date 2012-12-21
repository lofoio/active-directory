from models import Twitter
from django.shortcuts import render_to_response
from django.template import RequestContext


def public(request):
    return render_to_response('twitter/public.html',
            {'twitters': Twitter.objects.order_by('-date_posted'), },
            context_instance=RequestContext(request))
