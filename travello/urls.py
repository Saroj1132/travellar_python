from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('', views.index, name='index'),    
    path('index', views.index, name='index'),
    path('elements', views.elements, name='elements'),
    path('news', views.news, name='news'),
    path('destinations', views.destinations, name='destinations'),
    path('contact', views.contact, name='contact'),
    path('about', views.news, name='about'),

]