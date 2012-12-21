from django.shortcuts import render_to_response, redirect
import datetime


def home_page(response):
    return redirect("/blog/")


def static_page(response, template):
    template = "%s.html" % (template)
    return render_to_response(template)


def display_meta(request):
    values = request.META.items()
    values.sort()
    return render_to_response('info_meta.html', locals())


def debug(request):
    pass


def current_datetime(request):
    current_date = datetime.datetime.now()
#   assert False
    return render_to_response('current_datetime.html', locals())


def hours_ahead(request, hours_offset):
    next_time = datetime.datetime.now() + datetime.timedelta(hours = int(hours_offset))
    return render_to_response('hours_ahead.html', locals())
