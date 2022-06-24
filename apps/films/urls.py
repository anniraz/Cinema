from django.urls import path
from django.conf.urls import handler404

from apps.films.views import *

urlpatterns = [

    # path('',IndexView.as_view ,name='home'),
    path('detail/<int:id>',detailmovie ,name='detail_movie'),
    # path('booking_step1/',booking1 ,name='booking1'),
    # path('booking_step2/',booking2 ,name='booking2'),
    # path('booking_step3/',booking3 ,name='booking3'),
    path('',index ,name='home'),
    path('book/',BookingForm.as_view(), name='book'),
    path('news/', News_views.as_view(), name="news"),
    path('news_detail/<int:id>', News_detail.as_view(), name='news_detail'),
    path('movie_list/',movies,name='movie_list'),
    # path('main',main)
    path('register/',RegisterUser.as_view(), name='register'),
    path('login/',LoginUser.as_view(),name='login'),
    path('logout/', logout_user, name='logout'),
    path('contact/',contact,name='contact'),
    # path('404error/',error_404,name='404')
]


handler404='apps.films.views.error_404'


