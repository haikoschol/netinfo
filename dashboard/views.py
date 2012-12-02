#encoding: utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext

from .network_information import NetworkInformation

def dashboard(request):
    info = NetworkInformation()
    context = RequestContext(request, {
        u'interfaces': info.get_interfaces(),
        u'ssid': info.get_current_wifi_ssid(),
    })
    return render_to_response('dashboard.html', context)

