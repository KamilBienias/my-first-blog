from django.urls import path
from . import views

urlpatterns = [
    path('pass_text', views.search_text, name='search_text'),
    path('result_text', views.result_in_text, name='result_in_text'),
]
