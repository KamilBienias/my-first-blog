from django.urls import path
from . import views

urlpatterns = [
    path('pass_url', views.search_home_page_url, name='search_home_page_url'),
    path('pass_text', views.search_home_page_text, name='search_home_page_text'),
    path('result_url', views.result_in_url, name='result_in_url'),
    path('result_text', views.result_in_text, name='result_in_text'),
]