#encoding: utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext

from .network_information import get_interfaces

def dashboard(request):
    context = RequestContext(request, {u'interfaces': get_interfaces()})
    return render_to_response('dashboard.html', context)

