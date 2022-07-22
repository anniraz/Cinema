from django.db import models
from django.contrib.auth.models import User

from apps.films.models import Movie
from apps.home.models import Rooms



# Create your models here.
class ShowTime(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    room=models.ForeignKey(Rooms,on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    price=models.IntegerField(verbose_name='цена билета' )



    def __str__(self):
        return f'{self.movie} {self.room} - {self.date} : {self.time} '
    
class Seates(models.Model):

    seates_number=models.PositiveIntegerField()
    movie_name=models.ForeignKey(ShowTime ,on_delete=models.CASCADE )

 
        
    
    def __str__(self) :
        return f'{self.seates_number}  {self.movie_name}'
    

class Booking(models.Model):

    name = models.ForeignKey(User, on_delete=models.CASCADE)
    movie=models.ForeignKey(ShowTime,on_delete=models.CASCADE)
    seat = models.ForeignKey(Seates, on_delete=models.CASCADE)


    def __str__(self):
        return  f'{self.name}'
    class Meta:
        unique_together = ('seat', 'movie')

class BookedSeat(models.Model):

    seat = models.ForeignKey(Seates, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)


    class Meta:
        unique_together = ('seat', 'booking')

    def __str__(self):
        return str(self.seat) + '|' + str(self.booking)