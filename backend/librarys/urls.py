from os import path
from django.urls import path
from . import views as library_views

app_name = 'librarys'

urlpatterns = [
    path('', library_views.LibraryHomeView.as_view, name="home"),
    # path('search_result', )
]
