from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import LibraryPage, CommentReaction
from django.urls import reverse

# Create your views here.
class LibraryHomeView(ListView):
    model = LibraryPage
    template_name = "library_page.html"

class LibraryDetailView(DetailView):
    model = LibraryPage
    template_name = "post_detail.html"

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
    return render(request, 'search.html', context)

def LikeView(request, pk):
    like_library = get_object_or_404(CommentReaction, id=request.POST.get('post_id'))
    like_library.like.add(request.user)
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))

