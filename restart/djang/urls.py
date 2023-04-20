from .views import *
from django.urls import *

urlpatterns= [
    path('homepage', index, name='index'),
    path('about/', about, name='about'),
    path('help/', help, name='help')
]