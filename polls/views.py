from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question


class IndexView(generic.ListView):
    # domyślnie ListView używa <app name>/<model name>_list.html czyli u nas by było polls/question_list.html. Można to nadpisać w zmiennej template_name
    template_name = 'polls/index.html'
    # dla ListView automatycznie generowaną zmienną kontekstową jest question_list.
    # Nadpisujemy atrybut context_object_name i wskazujemy że chcemy użyć zamiast niej latest_question_list
    context_object_name = 'latest_question_list'

    # nadpisana metoda get_queryset(), która oryginalnie pobierałaby wszystkie pytania
    def get_queryset(self):
        """
            Return the last five published questions (not including those set to be
            published in the future). __lte oznacza lower than equal
            """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')[:5]

        # """Return the last five published questions."""
        # return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    # domyślnie DetailView używa <app name>/<model name>_detail.html czyli u nas by było polls/question_detail.html
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    # domyślnie DetailView używa <app name>/<model name>_detail.html czyli u nas by było polls/question_detail.html
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST to słownikowy obiekt, który daje dostęp do wysłanych danych według nazwy klucza.
        # W tym przypadku request.POST['choice'] zwraca ID wybranej odpowiedzi jako stringa.
        # Wartości request.POST są zawsze stringami.
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # request.POST['choice'] zgłosi KeyError jeśli atrybutu choice nie było wśród danych POST.
    # Sprawdza KeyError i ponownie wyświetla formularz pytania z komunikatem błędu,
    # jeśli choice nie został wskazany.
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form. Jeszcze raz wyświetla formularz głosowania
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "<h2 style='color:red;'> You didn't select a choice.</h2>",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# old views
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         'latest_question_list': latest_question_list
#     }
#     return render(request, 'polls/index.html', context)
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     context = {
#         'question': question
#     }
#     return render(request, 'polls/detail.html', context)
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     context = {
#         'question': question
#     }
#     return render(request, 'polls/results.html', context)