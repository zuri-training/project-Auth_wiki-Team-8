from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_view(request):
    # return render(request, 'home.html')
    return HttpResponse("Home page")


def about_view(request):
    # return render(request, 'about.html')
    return HttpResponse("About page")


def contact_view(request):
    # return render(request, 'contact.html')
    return HttpResponse("contact page")


def login_view(request):
    # return render(request, 'login.html')
    return HttpResponse("login page")


def register_view(request):
    # return render(request, 'registration.html')
    return HttpResponse("register page")
