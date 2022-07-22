from django.shortcuts import render
from .models import *

# # Create your views here.

def settings(request):

    settings=CinemaSettings.objects.latest('id')

    return render(request, 'index.html',{'settings':settings})



