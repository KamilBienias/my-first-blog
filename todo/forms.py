from django import forms
from todo.models import Task, Person


class PersonForm(forms.ModelForm):
    first_name = forms.CharField(label="Executor's first name", widget=forms.TextInput(
        attrs={"placeholder": "executor's first name"}))
    last_name = forms.CharField(label="Executor's last name", widget=forms.TextInput(
        attrs={"placeholder": "executor's last name"}))
    status = forms.ChoiceField(label="Executor's status", choices=Person.STATUS_CHOICES)

    class Meta:
        nazwa = forms.CharField(label='',
            widget=forms.TextInput(attrs={"placeholder": "Wpisz nazwę"}))  # etykieta Nazwa się nie pojawi bo label=''
        model = Person
        fields = [
            'first_name',
            'last_name',
            'status'
        ]


class TaskForm(forms.ModelForm):

    summary = forms.CharField(label="Summary of task", widget=forms.TextInput(
        attrs={"placeholder": "summary of task"}))
    description = forms.CharField(label="Description of task", widget=forms.TextInput(
        attrs={"placeholder": "description of task"}))
    importance = forms.DecimalField(label="Importance of task (1-9)")

    class Meta:
        nazwa = forms.CharField(label='',
            widget=forms.TextInput(attrs={"placeholder": "Wpisz nazwę"}))  # etykieta Nazwa się nie pojawi bo label=''
        model = Task
        fields = [
            'summary',
            'description',
            'importance'
        ]