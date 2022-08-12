from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm


def sendMail_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        message = 'Mail Sent. Thank you.'
        return render(request, "contactpage.html", {'msg': message})
    else:
        return render(request, "contactpage.html")
