from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render


def index(request):  # HttpRequest
    return HttpResponse("MyApp page")


def some_page(request):
    if request.POST:
        print(request.POST)
    return HttpResponse("<h1>It's some page</h1>")


def show_categories(request, cat_id):
    return HttpResponse(f"<h2>Categories: id={cat_id}</h2>")


def show_slug_categories(request, cat_slug):
    return HttpResponse(f"<h2>Categories: slug={cat_slug}</h2>")


def archive(request, year):
    if year > 2023:
        raise Http404()
    return HttpResponse(f"<h2>Archive of the year {year}</h2>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
