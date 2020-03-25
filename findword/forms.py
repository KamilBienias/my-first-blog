from django import forms
from .models import Findword


class FindwordForm(forms.ModelForm):
    text = forms.CharField(label="Pass the text to search", widget=forms.Textarea(
        attrs={"placeholder": "Some kind of text",
               "rows": 5,
               "cols": 70
               }))
    phrase = forms.CharField(label="Searched phrase", widget=forms.TextInput(
        attrs={"placeholder": "Some word"}))

    class Meta:
        nazwa = forms.CharField(label='',
            widget=forms.TextInput(attrs={"placeholder": "Wpisz nazwę"}))  # etykieta Nazwa się nie pojawi bo label=''
        model = Findword
        fields = [
            'text',
            'phrase',
        ]