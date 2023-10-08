from django.http import HttpResponse
from django.shortcuts import render


def index(request):  # HttpRequest
    return HttpResponse("MyApp page")


def some_page(request):
    return HttpResponse("<h1>It's some page</h1>")
