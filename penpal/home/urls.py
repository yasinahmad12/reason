from django.urls import path ,include 
from django.urls.resolvers import URLPattern


from . import views
from .views import *

urlpatterns = [
    path('', views.index),
    path('', views.home , name="home")
]