from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def drain(request):
  return HttpResponse('Drain Gang.')