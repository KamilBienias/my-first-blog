from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_home_page, name='search_home_page'),
    path('result', views.result, name='result'),
]