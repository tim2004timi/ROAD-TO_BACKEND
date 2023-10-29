from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

from myapp.models import Friends

menu = [
    {"title": "Главная страница", "name": "main"},
    {"title": "Войти", "name": "login"},
    {"title": "Друзья", "name": "friends"},
    {"title": "Добавить друга", "name": "add-friend"},
    {"title": "Обратная связь", "name": "feedback"},
    {"title": "О сайте", "name": "about"},
]


class MyClass:
    def __init__(self, x, y):
        self.x, self.y = x, y


def index(request):  # HttpRequest
    # t = render_to_string("myapp/index.html")
    # return HttpResponse(t)
    data = {
        "title": "Главная страница",
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


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def friends(request):
    friends_queryset = Friends.objects.all()

    print(friends_queryset[0].name)

    data = {
        "friends": friends_queryset,
        "title": "Друганы",
        "menu": menu,
    }
    return render(request, "myapp/friends.html", context=data)


def friend_slug(request, fr_slug):
    friend = get_object_or_404(Friends, slug=fr_slug)
    data = {"friend": friend,
            "title": friend.name,
            "menu": menu,
            }
    return render(request, "myapp/friend.html", data)


def add_friend(request):
    return HttpResponse("<h1>Добавить друга</h1>")


def feedback(request):
    return HttpResponse("<h1>Обратная связь</h1>")


def about(request):
    return HttpResponse("<h1>О сайте</h1>")


def login(request):
    return HttpResponse("<h1>Аутентификация</h1>")
