from django.urls import path, re_path, register_converter
from . import views
from .converter import FourDigitYearConverter


register_converter(FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index),  # http://127.0.0.1:8000/
    path('somepage/', views.some_page),  # http://127.0.0.1:8000/somepage/
    path("cats/<int:cat_id>/", views.show_categories),
    path("cats/<slug:cat_slug>/", views.show_slug_categories),
    path("archive/<year4:year>/", views.archive)
]
