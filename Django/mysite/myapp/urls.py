from django.urls import path, re_path, register_converter
from . import views
from .converter import FourDigitYearConverter


register_converter(FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name="main"),  # http://127.0.0.1:8000/
    path('somepage/', views.some_page, name="some"),  # http://127.0.0.1:8000/somepage/
    path("cats/<int:cat_id>/", views.show_categories, name="cat_id"),
    path("cats/<slug:cat_slug>/", views.show_slug_categories, name="cat_slug"),
    path("archive/<year4:year>/", views.archive, name="archive"),
    path("about/", views.about, name="about"),
]
