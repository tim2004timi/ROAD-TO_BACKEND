from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string


menu = ["О сайте", "Добавить друга", "Обратная связь", "Войти"]
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
    data = {
        "friends": [
            {"id": 1, "name": "Тима", "age": 19, "gender": "натурал", "the_best": True, "info": "<b>Тима</b> - это энергичный и творческий человек. Он всегда полон идей и стремится превратить каждый день в приключение. Возраст 19 лет - самый увлекательный период жизни, и Тима стремится извлечь максимум из каждой минуты. Он натурал и гордится своей индивидуальностью, не поддаваясь влиянию стереотипов. Тима - настоящий оптимист, который всегда готов поддержать друзей в трудную минуту. Его жизнерадостность и улыбка заразительны, и он всегда идет вперед, независимо от вызовов, с которыми он сталкивается."},
            {"id": 2, "name": "Вова", "age": 16, "gender": "натурал", "the_best": True, "info": "<b>Вова</b> - это умелый и ответственный молодой человек. В возрасте 16 лет, он уже проявил себя как талантливый индивидуалист. Вова - натурал, чья страсть к исследованию мира никогда не затухает. Он увлекается наукой и технологией, и его любопытство побуждает его исследовать новые горизонты. Независимо от возраста, Вова вдохновляет окружающих своими достижениями и умением преодолевать трудности. Его улучшенные навыки и стремление к самосовершенствованию делают его примером для всех, кто его окружает."},
            {"id": 3, "name": "Люба", "age": 17, "gender": "натурал", "the_best": False},
            {"id": 4, "name": "Пушок", "age": 12, "gender": "кот", "the_best": True, "info": "<b>Пушок</b> - это очаровательный и забавный кот. Ему всего 12 лет, но он уже завоевал множество сердец своей непередаваемой милотой. Пушок - представитель мирного мира, гендером которого является 'кот'. Он обладает невероятно пушистой шерстью и большими глазами, которые способны растопить даже самые холодные сердца. Пушок обожает греться на солнце, играть с мячиками и умилительно мурлыкать, когда его гладят. Его простая радость и беззаветная привязанность делают его идеальным спутником для всех, кто ищет тепло и радость в своей жизни."},
        ],
        "title": "Друганы",
        "menu": menu,
    }
    return render(request, "myapp/friends.html", context=data)


def add_friend(request):
    return HttpResponse("<h1>Добавить друга</h1>")


def feedback(request):
    return HttpResponse("<h1>Обратная связь</h1>")


def about(request):
    return HttpResponse("<h1>О сайте</h1>")


def login(request):
    return HttpResponse("<h1>Аутентификация</h1>")
