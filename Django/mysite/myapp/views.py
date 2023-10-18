from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string


menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


class MyClass:
    def __init__(self, x, y):
        self.x, self.y = x, y


def index(request):  # HttpRequest
    # t = render_to_string("myapp/index.html")
    # return HttpResponse(t)
    data = {
        "title": "главная страница",
        "menu": menu,
        "float": 28.55,
        "lst": [1, 2, 3, "abc", True],
        "set": {1, 2, 3},
        "dct": {"key1": "value1", "key2": "value2"},
        "obj": MyClass(10, 20),
    }
    return render(request, "myapp/index.html", context=data)


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
    if year < 2000:
        return HttpResponseRedirect("/")
        # return redirect("main", permanent=True)

    return HttpResponse(f"<h2>Archive of the year {year}</h2>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def about(request):
    data = {
        "friends": [
            {"name": "Тима", "age": 19, "gender": "натурал", "the_best": True},
            {"name": "Вова", "age": 16, "gender": "натурал", "the_best": True},
            {"name": "Люба", "age": 17, "gender": "натурал", "the_best": False},
            {"name": "Пушок", "age": 12, "gender": "кот", "the_best": True},
        ],
        "title": "О сайте"
    }
    return render(request, "myapp/about.html", context=data)
