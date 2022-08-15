from django.http import HttpResponse
from django.shortcuts import render
from librarys.models import LibraryPage


def solution(message, K):
    print(len(message))
    if len(message) < K:
        return message
    elif len(message) == K and message[-1] != ' ':
        return message[0: K]
    elif len(message) > K and message[K - 1] == ' ':
        return message[0: K - 1]
    elif message[K] == ' ':
        return message[0: K]
    else:
        i = K - 1
        while i < K:
            if message[i] == ' ':
                return message[0: i]
            i -= 1


def about(request):
    return render(request, 'aboutpage.html')


def home(request):
    library = LibraryPage.objects.all()[::-1]
    libraries = []
    if len(library) > 6:
        for i in range(6):
            libraries.append(library[i])
    else:
        libraries = library
    libraries1 = []
    if len(library) > 3:
        for i in range(3):
            library[i].description = solution(library[i].description, 150)
            libraries1.append(library[i])
    else:
        libraries1 = library
    return render(request, 'homepage.html', {'libraries': libraries, 'range': [1, 2, 3], 'libraries1': libraries1})


def contact_us(request):
    return render(request, 'contactpage.html')


def faq(request):
    return render(request, 'faqPage.html')
