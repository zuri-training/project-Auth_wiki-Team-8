from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # login(request, user)
            return redirect('dashboard:home')
        else:
            # print(form.errors.as_data())
            return render(request, 'accounts/registration.html', {'form': form})
    else:
        form = CustomUserCreationForm()
        return render(request, "accounts/registration.html", {'form': form})


def signin_view(request):
    # return render(request, 'homepage.html')
    return HttpResponse("Login page")


def logout_view(request):
    # return render(request, 'contactpage.html')
    return HttpResponse("Logout page")
