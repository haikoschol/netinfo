#encoding: utf-8
from django.shortcuts import render_to_response

from .network_information import get_interfaces

def dashboard(request):
    return render_to_response('dashboard.html', {u'interfaces': get_interfaces()})

