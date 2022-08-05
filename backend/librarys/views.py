from unicodedata import name
from django.views import View
from django.shortcuts import render
from .models import LibraryPage, CommentReaction


class LibrarySearchPage(View):
    def get(self, request, *args, **kwargs):
        if 'q' in request.GET:
            keyword = request.GET['q']
            libraries = LibraryPage.objects.filter(name__contains=keyword)
            found = len(libraries)
            return render(request, 'librarys/search_result.html', {'libraries': libraries, 'found': found, 'title': 'Search results'})
        else:
            return render(request, 'librarys/index.html')


class LibraryInfo(View):
    def get(self, request, *args, **kwargs):
        pk = request.GET.get('pk')
        library = LibraryPage.objects.filter(id=pk)
        return render(request, 'librarys/library_page.html', {'library': library})

