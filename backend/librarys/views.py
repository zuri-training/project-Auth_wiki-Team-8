from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Q
from django.views import View
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
from .models import LibraryPage, CommentReaction
from .forms import CommentForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

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
            except EmptyPage:
                libraries = libraries_per_page.page(page_num)
            except PageNotAnInteger:
                libraries = libraries_per_page.page(
                    libraries_per_page.num_pages)
            return render(
                request,
                'librarys/search_result.html',
                {
                    'libraries': libraries,
                    'found': found,
                    'title': 'Search results',
                    'page': libraries_per_page
                }
            )
        else:
            return redirect('/')


class LibraryInfo(View):
    def get(self, request, pk):
        library = LibraryPage.objects.get(id=pk)
        library.example_file = open(library.example_file.path, 'r')
        library.example_file = library.example_file.read()
        comments = CommentReaction.objects.filter(library=library)
        return render(
            request,
            'librarys/library_page.html',
            {
                'library': library,
                'comments': comments,
            }
        )

    def post(self, request, pk):
        library = LibraryPage.objects.get(id=pk)
        comment = CommentReaction(
            comment=request.POST['comment'], library=library, author=request.user)
        comment.save()
        return HttpResponseRedirect(request.path_info)


def dislikes(request, pk):
    if request.method == 'POST':
        library = LibraryPage.objects.get(id=pk)
        library.dislike += 1
        library.save()
    return HttpResponseRedirect(reverse('search_result', args=[str(pk)]))


def likes(request, pk):
    if request.method == 'POST':
        library = LibraryPage.objects.get(id=pk)
        library.like += 1
        library.save()
    return HttpResponseRedirect(reverse('search_result', args=[str(pk)]))


# class LibraryDetailView(DetailView):
#     model = LibraryPage
#     template_name = "library_detail.html"
#     slug_field = "slug"
#     form = CommentForm

#     def post(self, request, *args, **kwargs):
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             library = self.get_object()
#             form.instance.user =  request.user
#             form.instance.library = library
#             form.save()

#             return redirect(reverse('library_detail', kwargs= {
#                 'slug': library.slug
#             }))

#     def get_context_data(self, **kwargs):
#         library_comments_count = CommentReaction.objects.all().filter(library=self.object.id).count()
#         library_comments = CommentReaction.objects.all().filter(library=self.object.id)
#         context = super().get_context_data(**kwargs)

#         context.update({
#             'form': self.form,
#             'library_comments': library_comments,
#             'library_comments_count': library_comments_count,
#         })
#         return context


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
#     return render(request, 'search_result.html', context)
