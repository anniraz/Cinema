from django.urls import reverse
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=200)
    url = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name=models.CharField(max_length=250 ,null=True,blank=True,)

    def __str__(self):
        return self.name

class Director(models.Model):
    name=models.CharField(max_length=250,null=True,blank=True,)

    def __str__(self):
        return self.name



class Movie(models.Model):

    name=models.CharField(max_length=250 ,verbose_name='название фильма')
    country=models.CharField(max_length=100 ,verbose_name='страна')
    year=models.IntegerField(verbose_name='год')
    genre=models.ManyToManyField(Genre ,verbose_name='Жанры')
    category=models.ForeignKey(Category,on_delete=models.CASCADE , verbose_name='категории')
    director=models.ManyToManyField(Director ,verbose_name='директор' , related_name='director')
    actors=models.ManyToManyField(Actor ,verbose_name='актеры', related_name='actors')
    age_restriction=models.IntegerField(verbose_name='возрастное ограничение')
    date=models.ManyToManyField('Date',verbose_name='дата и время ')
    description=models.TextField(verbose_name='описание')
    poster=models.ImageField(upload_to='films_image/',verbose_name='постер')
    trailer=models.FileField(upload_to='trailer/',verbose_name='трейлер')
    url = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("detail_movie", kwargs={"id": self.id})
    
    class Meta:
        ordering=['-pk']
    
    
    
class Date(models.Model):

    date=models.DateTimeField( blank=True,null=True)


    def __str__(self):
        return f'{self.date} '


class Ticket(models.Model):

    price=models.IntegerField(blank=True,null=True ,verbose_name='цена билета для взрослых' )
    price_child=models.IntegerField(blank=True,null=True ,verbose_name='цена билета для детей ')
    movie_name=models.ForeignKey(Movie , on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.movie_name}  для взрослых {self.price} для детей {self.price_child} '


class Sites(models.Model):

    row=models.CharField(max_length=1 )
    sites_number=models.IntegerField()
    movie_name=models.ForeignKey(Movie ,on_delete=models.CASCADE )
    
    def __str__(self) :
        return f'{self.row}{self.sites_number}'

class Booking(models.Model):

    CHOICE=(('Детский','Детский'),('Взрослый','Взрослый'))
    name=models.CharField(max_length=200)
    email=models.EmailField(null=True,blank=True)
    ticket=models.ForeignKey(Ticket,on_delete=models.CASCADE)
    sites=models.ForeignKey(Sites,on_delete=models.CASCADE)
    ticket_choice=models.CharField(max_length=50,choices=CHOICE , verbose_name='Билет')

    def __str__(self):
        return self.name
    



    # class Meta:
    #     ordering = ["-value"]

class Reviews(models.Model):

    RATING = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    rating = models.IntegerField(choices=RATING, max_length=11)
    time_pub = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, verbose_name="фильм", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:

        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering=['-pk']

class ComingSoon(models.Model):

    name=models.CharField(max_length=250)
    poster=models.ImageField(upload_to='coming_soon/' ,null=True,blank=True)
    trailer=models.FileField(upload_to='trailer/',verbose_name='трейлер')

    def __str__(self):
        return self.name




class EndingSoon(models.Model):

    name=models.ForeignKey(Movie,on_delete=models.CASCADE)



class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    image = models.ImageField(upload_to=" news_images/", blank=True, null=True, verbose_name='Картина')
    description =   RichTextUploadingField(verbose_name='Описание')
    url = models.SlugField(null=True, unique=True, verbose_name='URL' )                                                                                                                                                                                                                      

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Новость'
        verbose_name_plural='Новости'
        ordering=['-pk']




    
    















