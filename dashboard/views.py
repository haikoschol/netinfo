#encoding: utf-8
from .network_information import NetworkInformation

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

import json

def dashboard(request):
    info = NetworkInformation()
    context = RequestContext(request, {
        u'interfaces': info.get_interfaces(),
        u'ssid': info.get_current_wifi_ssid(),
    })
    return render_to_response('dashboard.html', context)


def ssids(request):
   return HttpResponse(json.dumps(NetworkInformation().get_visible_wifi_ssids()),
       content_type='application/json')

