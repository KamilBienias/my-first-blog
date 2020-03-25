from django import forms
from search.models import Search
from search.models import Searchtext


class SearchForm(forms.ModelForm):
    website_address = forms.CharField(label="Website address", widget=forms.TextInput(
        attrs={"placeholder": "http://java4me.prv.pl/"}))
    passed_expression = forms.CharField(label="Pass expression you are looking for", widget=forms.TextInput(
        attrs={"placeholder": "Kamil"}))

    class Meta:
        nazwa = forms.CharField(label='',
            widget=forms.TextInput(attrs={"placeholder": "Wpisz nazwę"}))  # etykieta Nazwa się nie pojawi bo label=''
        model = Search
        fields = [
            'website_address',
            'passed_expression',
        ]


class SearchtextForm(forms.ModelForm):
    passed_text = forms.CharField(label="Pass the text to search", widget=forms.Textarea(
        attrs={"placeholder": "Some kind of text",
               "rows": 5,
               "cols": 70
               }))
    passed_phrase = forms.CharField(label="Searched phrase", widget=forms.TextInput(
        attrs={"placeholder": "Some word"}))

    class Meta:
        nazwa = forms.CharField(label='',
            widget=forms.TextInput(attrs={"placeholder": "Wpisz nazwę"}))  # etykieta Nazwa się nie pojawi bo label=''
        model = Searchtext
        fields = [
            'passed_text',
            'passed_phrase',
        ]