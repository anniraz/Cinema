from django.db import models

# Create your models here.
class Rooms(models.Model):
    rooms=models.PositiveIntegerField(verbose_name='комната')

    def __str__(self):
        return f'№{self.rooms}'


class CinemaSettings(models.Model):
    
    title = models.CharField(verbose_name="Название кинотеатра",  max_length=50,null=True,blank=True)
    rooms=models.ManyToManyField(Rooms,verbose_name='комнаты')
    logo = models.ImageField(verbose_name="Логотип сайта",upload_to='images/',null=True,blank=True)
    header_logo = models.ImageField(verbose_name="Header image",upload_to='header_images/',null=True,blank=True)
    description = models.CharField(verbose_name="Описание сайта",max_length=255 ,null=True,blank=True)
    address = models.CharField(verbose_name="Адрес сайта",max_length=100 ,null=True,blank=True)
    phone = models.CharField(verbose_name="телефон",max_length=15,null=True,blank=True)
    email = models.CharField(max_length=50,null=True,blank=True)
    facebook = models.CharField(help_text="ссылка на facebook", max_length=150,null=True,blank=True)
    instagram = models.CharField(help_text="ссылка на instagram",max_length=150,null=True,blank=True)
    twitter = models.CharField(help_text="ссылка на twitter",max_length=150,null=True,blank=True)
    telegram = models.CharField(help_text="ссылка на telegram", max_length=150,null=True,blank=True)

    def __str__(self):
        return f"ID: {self.id} / {self.title}"
    
    class Meta:
        
        ordering=['-id']
        verbose_name_plural = "Основные настройки сайта"





