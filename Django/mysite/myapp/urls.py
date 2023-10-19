from django.urls import path, re_path, register_converter
from . import views
from .converter import FourDigitYearConverter


register_converter(FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name="main"),  # http://127.0.0.1:8000/
    path('somepage/', views.some_page, name="some"),  # http://127.0.0.1:8000/somepage/
    path("friends/", views.friends, name="friends"),
    path("add-friend/", views.add_friend, name="add-friend"),
    path("feedback/", views.feedback, name="feedback"),
    path("about/", views.about, name="about"),
    path("login/", views.login, name="login")
]
