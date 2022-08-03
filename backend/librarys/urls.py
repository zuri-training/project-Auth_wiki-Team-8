from os import path
from django.urls import path
from . import views

app_name = 'librarys'

urlpatterns = [
    path('home/', views.library_view, name="home"),
]
