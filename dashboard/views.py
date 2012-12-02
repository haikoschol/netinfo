from django.shortcuts import render_to_response

def dashboard(request):
    interfaces = [{'name': 'eth0'}, {'name': 'eth1'}]
    return render_to_response('dashboard.html', {'interfaces': interfaces})

