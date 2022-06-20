from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import generic
from apps.films.forms import BookingForm,ReviewForm
from django.db.models import Q
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login

from apps.films.models import *
from .forms import *
from django.views.generic.base import View

class LoginUser(LoginView):
    form_class=LoginUserForm
    template_name='cinematempl/login.html'
    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUser(generic.CreateView):
    form_class=RegisterUserForm
    template_name='cinematempl/register.html'
    success_url=reverse_lazy('home')

    def form_valid(self,form):
        user=form.save()
        login(self.request,user)
        return redirect('home')

def logout_user(request):
    logout(request)
    return redirect('home')

# class DetailMovie(generic.DetailView):
#     model=Movie
#     template_name='cinematempl/movie_page_detail.html'
#     pk_url_kwarg='id'
#     context_object_name='movie'

def detailmovie(request,id):
    movie=Movie.objects.get(id=id)
    review=Reviews.objects.filter(movie_id=movie)[:5]
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
              form = form.save(commit=False)
              form.movie = movie
              form.save()
              return redirect('home')


    else:
        form = ReviewForm()

    context={
        'movie':movie,
        'form': form,
        'review':review
        }
    return render(request,'cinematempl/movie_page_detail.html',context)




class BookingForm(generic.CreateView):
    form_class=BookingForm
    template_name='cinematempl/book.html'
    success_url=reverse_lazy('book')


    # def get_context_data(self, **kwargs):
    #     context=super().get_context_data(**kwargs)
    #     context['movies']=Movie.objects.all()


class News_views(generic.ListView):
    model=News
    template_name='cinematempl/news.html'
    context_object_name='news'

class Movies(generic.ListView):
    model=News
    template_name='cinematempl/movie_list.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['movies']=Movie.objects.all()

def movies(request):
    movies=Movie.objects.all()
    context={'movies':movies}
    return render(request,'cinematempl/movie_list.html',context)



class News_detail(generic.DetailView):
    model=News
    template_name='cinematempl/news_detail.html'
    pk_url_kwarg='id'
    context_object_name='news'






# def booking1(request):
#     movies=Movie.objects.all()[:7]
#     context={'movies':movies}
#     return render(request,'cinema_booking/book1.html',context)

# def booking2(request):
#     sits=Sites.objects.all()
#     context={'sits':sits}
#     return render(request,'cinema_booking/book2.html',context)

# def booking3(request):
#     return render(request,'cinema_booking/book3-buy.html')






def index(request):
    endingsoon=EndingSoon.objects.all()
    movie_slider=Movie.objects.all()[:3]
    movie1=Movie.objects.all()[:1]
    movies=Movie.objects.all()[1:2]
    movie3=Movie.objects.all()[2:3]
    movie4=Movie.objects.all()[3:4]
    movie5=Movie.objects.all()[4:5]
    movie6=Movie.objects.all()[5:6]
    news=News.objects.all()[:9]

    if 'search_button' in request.GET:
        word = request.GET.get('search-input')
        movie_all = Movie.objects.filter(Q(name__icontains=word))
        return render(request, 'index.html', {'movie_all': movie_all})
    else:
        movie_all=Movie.objects.all()[:6]

    context={
        'movies':movies,
        'movie_all':movie_all,
        'movie1':movie1,
        'movie3':movie3,
        'movie4':movie4,
        'movie5':movie5,
        'movie6':movie6,
        'endingsoon':endingsoon,
        'news':news,
        'movie_slider':movie_slider

    }
    
    return render(request,'index.html',context)
