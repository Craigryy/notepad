from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def get_note(request,id=None):
    message = f'you submitted id: {id}'
    return HttpResponse(message)