from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return render(request, 'aboutpage.html')


def home(request):
    return render(request, 'homepage.html')


def contact_us(request):
    return render(request, 'contactpage.html')


def faq(request):
    return render(request, 'faqPage.html')
