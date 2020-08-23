from django.urls import path
from . import views

app_name = "ipcalculator"

urlpatterns = [
    path('', views.pass_method, name='pass_name'),
    path('solution_ip/', views.solution_method, name='solution_name'),
]
