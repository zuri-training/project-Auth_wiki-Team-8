from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import LibraryPage, CommentReaction

# Create your views here.
class LibraryHomeView(ListView):
    model = LibraryPage
    template_name = "library_page.html"

class LibraryDetailView(DetailView):
    model = LibraryPage
    template_name = "Post_Detail.html"

