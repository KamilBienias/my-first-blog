from django import forms
from search.models import Search


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