import mimetypes
import os
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Q
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import LibraryPage, CommentReaction
from .forms import CommentForm
from django.urls import reverse

# Create your views here.
class LibraryHomeView(ListView):
    model = LibraryPage
    template_name = "librarys/library_page.html"

class LibraryDetailView(DetailView):
    model = LibraryPage
    template_name = "library_detail.html"
    slug_field = "slug"
    form = CommentForm

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            library = self.get_object()
            form.instance.user =  request.user
            form.instance.library = library
            form.save()

            return redirect(reverse('library_detail', kwargs= {
                'slug': library.slug
            }))

    def get_context_data(self, **kwargs):
        library_comments_count = CommentReaction.objects.all().filter(library=self.object.id).count()
        library_comments = CommentReaction.objects.all().filter(library=self.object.id)
        context = super().get_context_data(**kwargs)

        context.update({
            'form': self.form,
            'library_comments': library_comments,
            'library_comments_count': library_comments_count,
        })
        return context


def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search').split(" ")
        for searched in search:
            libraries = LibraryPage.objects.all().filter(
                Q(name__icontains=searched) |
                Q(description__icontains=searched) |
                Q(library_language__icontains=searched)
                ).distinct()
    else:
        libraries = LibraryPage.objects.all()
    context = {
        'libraries': libraries
    }
    return render(request, 'search_result.html', context)







