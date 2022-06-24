from django.contrib import admin
from modeltranslation.admin import TranslationAdmin


from .models import *

# Register your models here.


class MovieAdmin(TranslationAdmin):
    list_display = ('name', 'year','id')
    prepopulated_fields = {'url':('name',)}

admin.site.register(Movie,MovieAdmin)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url':('name',)}

admin.site.register(Category,CategoryAdmin)

class TicketAdmin(admin.ModelAdmin):
    list_display=('movie_name','price','price_child')

admin.site.register(Ticket,TicketAdmin)


class NewsAdmin(TranslationAdmin):
        prepopulated_fields = {'url':('title',)}

admin.site.register(News,NewsAdmin)



admin.site.register(Genre )
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Sites)
admin.site.register(Booking)
admin.site.register(Reviews)
admin.site.register(Date)
admin.site.register(ComingSoon)
admin.site.register(EndingSoon)
admin.site.register(Contact)
