from django.shortcuts import render, redirect
from .models import Findword
from .forms import FindwordForm
import re

def search_text(request):
    form = FindwordForm(
        request.POST or None)  # jeśli metoda POST to renderuj ten formularz a jeśli nie ma danych to renderuj pusty formularz
    if form.is_valid():
        form.save(commit=True)
        # form = FindwordForm()  # odświeża formularz, po zapisaniu będą puste pola. To już niepotrzebne, bo po wysłaniu przenosi na inną stronę
        return redirect("/findword/result_text")
    context = {
        'form': form
    }
    return render(request, "findword/search_text.html", context)


def result_in_text(request):
    searches = Findword.objects.all()
    searches_ids = []
    for search in searches:
        searches_ids.append(search.id)

    added_search = Findword.objects.get(id=searches_ids[-1])

    result_of_searching = re.findall(added_search.phrase, added_search.text)

    how_many_times = len(result_of_searching)

    context = {
        'added_search': added_search,
        'how_many_times': how_many_times
    }

    return render(request, "findword/result_in_text.html", context)