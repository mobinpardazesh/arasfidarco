from django.shortcuts import render
from rest_framework import viewsets
from django.core.mail import EmailMessage
import consult
from django.core.mail import EmailMessage, get_connection
from django.conf import settings
from .forms import Customerform



# Create your  views here.
def home(request):
    form = Customerform()
    if request.method == "POST":
        form = Customerform(request.POST)
        if form.is_valid():
            form.save()
        # else:
        #     form = Customerform
        # context = {}
        # context['form'] = Customerform()

    context = {'form': form}
    return render(request, "home.html", {context})


def ru(request):
    return render(request, "ru.html", {})


def ar(request):
    return render(request, "ar.html", {})


def tr(request):
    return render(request, "tr.html", {})


def iso9001(request):
    return render(request, "iso9001.html", {})


def iso10002(request):
    return render(request, "iso10002.html", {})


def iso10004(request):
    return render(request, "iso10004.html", {})


def enexportnews(request):
    return render(request, "enexportnews.html", {})


def enindustrynews(request):
    return render(request, "enindustrynews.html", {})


def eneconomicsnews(request):
    return render(request, "eneconomicsnews.html", {})


def news(request):
    return render(request, "news.html", {})
