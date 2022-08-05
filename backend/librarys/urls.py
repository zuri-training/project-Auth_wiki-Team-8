from os import path
from django.urls import path
from . import views as library_views

app_name = 'librarys'

urlpatterns = [
    path('', library_views.LibrarySearchPage, name="home"),
    path('search_result/<pk>', library_views.LibraryInfo, name='search_result')
]
