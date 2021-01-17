from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.books_short, name='index'),
    path('homework02/', views.homework02, name='homework02'),
    path('homework03/', views.homework03, name='homework03'),
]