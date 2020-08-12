from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path('', views.todo_home_page_method, name='todo_home_page'),
    path('persons/', views.all_persons_method, name='all_persons'),
    path('persons/<int:id>/tasks/', views.tasks_of_chosen_person_method, name='tasks_of_chosen_person'),
    path('person/new/', views.create_person_method, name='create_person'),
    path('person/new/added/', views.create_person_added_method, name='create_person_added'),
    path('person/remove/', views.remove_person_method, name='remove_person'),
    path('person/remove/<int:id>', views.remove_person_deleted_method, name='remove_person_deleted'),
    path('person/assign/', views.person_assign_method, name='person_assign'),
    path('person/assign/<int:person_id>', views.person_assign_task_method, name='person_assign_task'),
    path('person/assign/<int:person_id>/<int:task_id>', views.person_assign_task_chosen_method, name='person_assign_task_chosen'),
    path('tasks/', views.all_tasks_method, name='all_tasks'),
    path('task/new/', views.create_task_method, name='create_task'),
    path('task/new/added/', views.create_task_added_method, name='create_task_added'),
    path('task/remove/', views.remove_task_method, name='remove_task'),
    path('task/remove/<int:id>', views.remove_task_deleted_method, name='remove_task_deleted'),
]
