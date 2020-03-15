from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):  # sposób tabelaryczny bardziej zwarty niż admin.StackedInline
    model = Choice
    extra = 3  # domyślnie wyświetl pola na 3 wybory


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]  # obiekty Choice są edytowane na stronie admina Question.
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']  # po prawej str dodaje filtr listy obiektów używając pola pub_date
    search_fields = ['question_text']  # To dodaje pole wyszukiwania (z lupą) na górze „change listy”


admin.site.register(Question, QuestionAdmin)
