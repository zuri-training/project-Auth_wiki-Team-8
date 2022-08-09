from os import path
from django.urls import path
from . import views as library_views

app_name = 'librarys'

urlpatterns = [
    path('', library_views.LibrarySearchPage.as_view(), name="home"),
    path('dislike/<pk>', library_views.dislikes, name='dislike'),
    path('like/<pk>', library_views.likes, name='like'),
    path('search_result/<pk>', library_views.LibraryInfo.as_view(),
         name='search_result'),
]
