from django.urls import path
from . import views

app_name = "findword"

urlpatterns = [
    path('', views.search_text_method, name='search_text_name'),
    path('result_text/', views.result_in_text_method, name='result_in_text_name'),
]
