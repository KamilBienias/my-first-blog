from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'), # Django spodziewa się liczby całkowitej i przekaże jej wartość do widoku jako zmienną pk
]