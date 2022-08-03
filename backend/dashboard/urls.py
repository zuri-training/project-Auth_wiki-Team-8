from os import path
from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('home/', views.home_view, name="home"),
]
