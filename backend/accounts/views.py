from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm, CustomUserAuthenticationForm, CustomUserChangeForm


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard:home')
        else:
            # print(form.errors.as_data())
            return render(request, 'accounts/registration.html', {'form': form})
    else:
        form = CustomUserCreationForm()
        return render(request, "accounts/registration.html", {'form': form})


def signin_view(request):
    if request.method == 'POST':
        form = CustomUserAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('dashboard:home')
        else:
            return render(request, 'accounts/login.html', {'form': form})
    else:
        form = CustomUserAuthenticationForm()
    return render(request, "accounts/login.html", {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts/login.html')
    else:
        return redirect('accounts/login.html')


def profile_view(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('dashboard:home')
        else:
            print(form.errors.as_data())
            return render(request, 'accounts/edit_profile.html', {'form': form})
    else:
        form = CustomUserChangeForm(instance=request.user)
        return render(request, "accounts/edit_profile.html", {'form': form})


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'accounts/change_pass.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('dashboard:home')
