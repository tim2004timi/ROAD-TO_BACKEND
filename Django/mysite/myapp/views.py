from django.http import HttpResponse
from django.shortcuts import render


def index(request):  # HttpRequest
    return HttpResponse("MyApp page")


def some_page(request):
    return HttpResponse("<h1>It's some page</h1>")


def show_categories(request, cat_id):
    return HttpResponse(f"<h2>Categories: id={cat_id}</h2>")


def show_slug_categories(request, cat_slug):
    return HttpResponse(f"<h2>Categories: slug={cat_slug}</h2>")


def archive(request, year):
    return HttpResponse(f"<h2>Archive of the year {year}</h2>")
