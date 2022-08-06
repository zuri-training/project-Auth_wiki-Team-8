from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.views import View
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
from .models import LibraryPage, CommentReaction
from django.urls import reverse

# Create your views here.
# class LibraryHomeView(ListView):
#     model = LibraryPage
#     template_name = "library_page.html"

# class LibraryDetailView(DetailView):
#     model = LibraryPage
#     template_name = "post_detail.html"

# def searchbar(request):
#     if request.method == 'GET':
#         search = request.GET.get('search').split(" ")
#         for searched in search:
#             libraries = LibraryPage.objects.all().filter(
#                 Q(name__icontains=searched) |
#                 Q(description__icontains=searched) |
#                 Q(library_language__icontains=searched)
#                 ).distinct()
#     else:
#         libraries = LibraryPage.objects.all()
#     context = {
#         'libraries': libraries
#     }
#     return render(request, 'search.html', context)

class LibrarySearchPage(View):
    def get(self, request, *args, **kwargs):
        if 'q' in request.GET:
            keyword = request.GET.get('q', '')
            # libraries = LibraryPage.objects.filter(name__contains=keyword)
            libraries = LibraryPage.objects.filter(
                Q(name__icontains=keyword) |
                Q(description__icontains=keyword) |
                Q(library_language__icontains=keyword)
                )
            found = len(libraries)
            page_num = 7
            page = request.GET.get('page', 1)
            libraries_per_page = Paginator(libraries, page_num)
            try:
                libraries = libraries_per_page.page(page)
            except PageNotAnInteger:
                libraries = libraries_per_page.page(page_num)
            except EmptyPage:
                libraries = libraries_per_page.page(libraries_per_page.num_pages)
            return render(request, 'librarys/search_result.html', {'libraries': libraries, 'found': found, 'title': 'Search results'})
        else:
            return render(request, 'librarys/index.html')


class LibraryInfo(View):
    def get(self, request, *args, **kwargs):
        pk = request.GET.get('pk')
        library = LibraryPage.objects.filter(id=pk)
        return render(request, 'librarys/library_page.html', {'library': library})



def LikeView(request, pk):
    like_library = get_object_or_404(CommentReaction, id=request.POST.get('post_id'))
    like_library.like.add(request.user)
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))
