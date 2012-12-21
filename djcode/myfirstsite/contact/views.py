from django.core.mail import send_mail
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from myfirstsite.contact.forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'localhost@localhost.com'),
                ['wangdian@localhost6.localdomain6'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'I love your site!'}
        )
    return render_to_response('contact_form.html', {'form': form},
                    context_instance=RequestContext(request))


def thanks(request):
    return render_to_response('thanks.html')
