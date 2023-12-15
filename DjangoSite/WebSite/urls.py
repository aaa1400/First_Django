from django.urls import path
from .views import *
from django.contrib import admin


app_name = 'WebSite'


urlpatterns = [
    path('', index_view, name='index'),
    path('about/', about_view, name='about'),
    path('contact/', contactUs_view, name='contact'),
    path('newsletter/', newsletter_view, name='newsletter'),
]
