from django.shortcuts import render, redirect

from search.models import Search
from search.forms import SearchForm

from urllib.request import urlopen
import re


def search_home_page(request):
    form = SearchForm(
        request.POST or None)  # jeśli metoda POST to renderuj ten formularz a jeśli nie ma danych to renderuj pusty formularz
    if form.is_valid():
        form.save(commit=True)
        # form = SearchForm()  # odświeża formularz, po zapisaniu będą puste pola. To już niepotrzebne, bo po wysłaniu przenosi na inną stronę
        return redirect("/search/result")
    context = {
        'form': form
    }
    return render(request, "search/search.html", context)


def result(request):

    # searches = Search.objects.all()
    # searches_ids = []
    # for search in searches:
    #     searches_ids.append(search.id)
    #
    # added_search = Search.objects.get(id=searches_ids[-1])
    #
    # with urlopen(added_search.website_address) as web_response:
    #     source = web_response.read()
    #
    # source_as_string = str(source)
    #
    # result_of_searching = re.findall(added_search.passed_expression, source_as_string)
    #
    # how_many_times = len(result_of_searching)
    #
    # context = {
    #     'added_search': added_search,
    #     'how_many_times': how_many_times
    # }


    # passed_url = input("Pass url: ")
    passed_url = "http://java4me.prv.pl"

    with urlopen(passed_url) as response:
        source = response.read()

    source_as_string = str(source)
    # print("Shows whole site as string")
    # print(source_as_string)
    # passed_expression = input("Pass expression you are looking for: ")
    passed_expression = "Kam"
    result_of_searching = re.findall(passed_expression, source_as_string)
    how_many_times = len(result_of_searching)
    context = {
        'passed_url': passed_url,
        'passed_expression': passed_expression,
        'how_many_times': how_many_times
    }

    return render(request, "search/result.html", context)

