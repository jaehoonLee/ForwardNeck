from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.
def main(request):
  return render_to_response('index.html', RequestContext(request))

def main2(request):
  return render_to_response('index3.html', RequestContext(request))

def main3(request):
  return render_to_response('index2.html', RequestContext(request))

def tracking(request):
  return render_to_response('tracking.html', RequestContext(request))