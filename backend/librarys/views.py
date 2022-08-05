from unicodedata import name
from django.views import View
from django.shortcuts import render
from .models import LibraryPage, CommentReaction


class LibrarySearchPage(View):
    def get(self, request, *args, **kwargs):
        if 'q' in request.GET:
            keyword = request.GET['q']
            libraries = LibraryPage.objects.filter(name__contains=keyword)
            return render(request, 'librarys/library_page.html', {'libraries': libraries})
        else:
            return render(request, 'librarys/index.html')


class LibraryInfo(View):
    def get(self, request, *args, **kwargs):
        pk = request.GET.get('pk')
        library = LibraryPage.objects.filter(id=pk)
        return render(request, 'librarys/search_result.html', {'library': library})

