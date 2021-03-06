from django.shortcuts import render, get_object_or_404, redirect
from todo.models import Task, Person
from django.http import HttpResponse
from todo.forms import PersonForm, TaskForm


# /
def todo_home_page_method(request):
    return render(request, "todo/todo.html")


# persons/
def all_persons_method(request):
    """ shows list of all persons """
    all_persons_list = Person.objects.order_by('id')
    context = {
        'all_persons_list': all_persons_list
    }
    return render(request, "todo/persons/allpersons.html", context)


# persons/<int:id>/tasks/
def tasks_of_chosen_person_method(request, id):
    """ From list of all persons you can select tasks of chosen person.
     Do that by clicking link: View all tasks of executor with id=(id given in url)"""
    chosen_person = Person.objects.get(id=id)  # get person which id is as given in url
    all_tasks_list = Task.objects.all()
    tasks_assigned_to_some_person = []  # there will be tasks assigned to any person
    for task in all_tasks_list:
        if task.person is not None:  # if task is assigned to any person
            tasks_assigned_to_some_person.append(task)  # then add that task to tasks_assigned_to_some_person list

    tasks_list_of_chosen_person = []  # there will be tasks assigned to chosen person
    for task in tasks_assigned_to_some_person:  # iterates tasks from tasks which are assign to any person (to avoid null pointer in line below)
        if task.person.id == chosen_person.id:  # if task has assign the same person which is chosen_person
            tasks_list_of_chosen_person.append(task)  # add that task to tasks of chosen person
    context = {
        'chosen_person': chosen_person,
        'tasks_list_of_chosen_person': tasks_list_of_chosen_person
    }
    return render(request, "todo/persons/tasksofchosenperson.html", context)


# person/new/
def create_person_method(request):
    form = PersonForm(
        request.POST or None)  # jeśli metoda POST to renderuj ten formularz a jeśli nie ma danych to renderuj pusty formularz
    if form.is_valid():
        form.save(commit=True)
        # form = BookForm()  # odświeża formularz, po zapisaniu będą puste pola. To już niepotrzebne, bo po wysłaniu przenosi na inną stronę
        return redirect("/todo/person/new/added/")
    context = {
        "form": form
    }
    return render(request, "todo/persons/createperson.html", context)


# person/new/added/
def create_person_added_method(request):
    persons = Person.objects.all()
    persons_ids = []
    for person in persons:
        persons_ids.append(person.id)

    added_person = Person.objects.get(id=persons_ids[-1])

    context = {
        'added_person': added_person
    }
    return render(request, "todo/persons/createpersonadded.html", context)


# person/remove/
def remove_person_method(request):
    all_persons_list = Person.objects.order_by('id')
    context = {
        'all_persons_list': all_persons_list
    }
    return render(request, "todo/persons/removeperson.html", context)


# person/remove/<int:id>
def remove_person_deleted_method(request, id):
    person_non_grata = get_object_or_404(Person, id=id)
    person_non_grata.delete()
    context = {
        'person_non_grata': person_non_grata,
        'its_id': id
    }
    return render(request, "todo/persons/removepersondeleted.html", context)

# person/assign/
def person_assign_method(request):
    """ Shows list of all persons but only available persons can assing new tasks """
    all_persons_list = Person.objects.order_by('id')
    context = {
        'all_persons_list': all_persons_list
    }
    return render(request, "todo/persons/personassign.html", context)


# person/assign/<int:person_id>
def person_assign_task_method(request, person_id):
    """ For chosen executor (with person_id) shows list of tasks which have no executors """
    all_tasks_list = Task.objects.order_by('id')
    tasks_unassigned_to_any_person_list = []
    for task in all_tasks_list:
        if task.person is None:
            tasks_unassigned_to_any_person_list.append(task)
    context = {
        'tasks_unassigned_to_any_person_list': tasks_unassigned_to_any_person_list,
        'person_id': person_id
    }
    return render(request, "todo/persons/personassigntask.html", context)


# person/assign/<int:person_id>/<int:task_id>
def person_assign_task_chosen_method(request, person_id, task_id):
    chosen_person = Person.objects.get(id=person_id)
    chosen_task = Task.objects.get(id=task_id)
    chosen_task.person = chosen_person
    chosen_task.save()
    chosen_person.save()
    context = {
        'chosen_task': chosen_task
    }
    return render(request, "todo/persons/personassigntaskchosen.html", context)


# tasks/
def all_tasks_method(request):
    all_tasks_list = Task.objects.order_by('id')
    context = {
        'all_tasks_list': all_tasks_list
    }
    return render(request, "todo/tasks/alltasks.html", context)


# task/new/
def create_task_method(request):
    form = TaskForm(
        request.POST or None)  # jeśli metoda POST to renderuj ten formularz a jeśli nie ma danych to renderuj pusty formularz
    if form.is_valid():
        form.save(commit=True)
        # form = BookForm()  # odświeża formularz, po zapisaniu będą puste pola. To już niepotrzebne, bo po wysłaniu przenosi na inną stronę
        return redirect("/todo/task/new/added/")
    context = {
        "form": form
    }
    return render(request, "todo/tasks/createtask.html", context)


# task/new/added/
def create_task_added_method(request):
    tasks = Task.objects.all()
    tasks_ids = []
    for task in tasks:
        tasks_ids.append(task.id)

    added_task = Task.objects.get(id=tasks_ids[-1])

    context = {
        'added_task': added_task
    }
    return render(request, "todo/tasks/createtaskadded.html", context)


# task/remove/
def remove_task_method(request):
    all_tasks_list = Task.objects.order_by('id')
    context = {
        'all_tasks_list': all_tasks_list
    }
    return render(request, "todo/tasks/removetask.html", context)


# task/remove/<int:id>
def remove_task_deleted_method(request, id):
    task_non_grata = get_object_or_404(Task, id=id)
    task_non_grata.delete()
    context = {
        'task_non_grata': task_non_grata,
        'its_id': id
    }
    return render(request, "todo/tasks/removetaskdeleted.html", context)
