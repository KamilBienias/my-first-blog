from django.urls import path
from . import views

app_name = "iss"

urlpatterns = [
    path('', views.iss_home_page_method, name='iss_home_page'),
]
