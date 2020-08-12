from django.contrib import admin
from .models import Task, Person

admin.site.register(Task)
admin.site.register(Person)

# @admin.register(Person)
# class PersonAdmin(admin.ModelAdmin):
#     list_display = {'id', 'first_name', 'last_name', 'status'}
#     list_filter = {'id', 'first_name', 'last_name', 'status'}
#     search_fields = {'first_name', 'last_name', 'status'}
