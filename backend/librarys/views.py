from django.http import HttpResponse
# from django.shortcuts import render


def library_view(request):
    # return render(request, 'aboutpage.html')
    return HttpResponse("Library page")