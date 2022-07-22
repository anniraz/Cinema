from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import *
from apps.films.models import *
from apps.home.models import *
from .models import *


# Create your views here.

def booking1(request):
    movies=Movie.objects.all()[:7]
    context={'movies':movies}
    return render(request,'cinema_booking/book1.html',context)

def booking2(request,id):

    sits=Seates.objects.filter(movie_name__id=id)
    # book=Booking.objects.get(movie__id=id)
    context={'sits':sits}
    return render(request,'cinema_booking/book2.html',context)

def booking3(request):
    return render(request,'cinema_booking/book3-buy.html')

class BookingForm(generic.CreateView):
    form_class=BookingForm
    template_name='cinematempl/book.html'
    success_url=reverse_lazy('book')

