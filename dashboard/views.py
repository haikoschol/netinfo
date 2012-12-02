#encoding: utf-8
from django.shortcuts import render_to_response

def dashboard(request):
    interfaces = [{
            u'name': u'eth0', 
            u'type': u'ethernet',
            u'state': u'activated',
            u'ip4_addresses': [u'10.0.0.23', u'192.168.1.2'],
            u'ip6_addresses': [],
        },
        {
            u'name': u'eth1',
            u'type': u'wifi',
            u'state': u'unavailable',
            u'ip4_addresses': [u'10.0.1.42'],
            u'ip6_addresses': [],
        },
    ]
    return render_to_response('dashboard.html', {u'interfaces': interfaces})

