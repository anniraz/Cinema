from django.urls import path
from .views import *

# from apps.films.views import *

urlpatterns = [
    path('book/',BookingForm.as_view(),name='book'),
    path('booking_step1/',booking1 ,name='booking1'),
    path('booking_step2/<int:id>/',booking2 ,name='booking2'),
    path('booking_step3/',booking3 ,name='booking3'),

]