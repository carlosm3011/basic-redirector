from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
import time 

from brapp.models import *

# Create your views here.

def redirect(request, short_code):

    try:
        url = get_object_or_404(Url, short_code = short_code)
        #
        # return HttpResponse(f"dest: {url.destination_url}")
        h1 = Hit(timestamp=time.time(), short_code=short_code)
        h1.save()
        return HttpResponseRedirect(url.destination_url)
    except Http404:
        h1 = Hit(timestamp=time.time(), short_code='_http404')
        h1.save()
        return HttpResponse(f"<h2>esa url :{short_code}: no existe</h2>")
    except: 
        raise
# end redirect

