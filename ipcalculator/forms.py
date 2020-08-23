from django import forms
from .models import HostAndMask


class HostAndMaskForm(forms.ModelForm):
    host_octet_1 = forms.DecimalField(label="Host's octet 1",
                                      # widget=forms.DecimalField(max_value=255,
                                      #                           min_value=0,
                                      #                           max_digits=3,
                                      #                           decimal_places=0)
                                      )
    host_octet_2 = forms.DecimalField(label="Host's octet 2",
                                      # widget=forms.DecimalField(max_value=255,
                                      #                           min_value=0,
                                      #                           max_digits=3,
                                      #                           decimal_places=0)
                                      )
    host_octet_3 = forms.DecimalField(label="Host's octet 3",
                                      # widget=forms.DecimalField(max_value=255,
                                      #                           min_value=0,
                                      #                           max_digits=3,
                                      #                           decimal_places=0)
                                      )
    host_octet_4 = forms.DecimalField(label="Host's octet 4",
                                      # widget=forms.DecimalField(max_value=255,
                                      #                           min_value=0,
                                      #                           max_digits=3,
                                      #                           decimal_places=0)
                                      )

    mask_octet_1 = forms.DecimalField(label="Mask's octet 1",
                                      # widget=forms.DecimalField(max_value=255,
                                      #                           min_value=0,
                                      #                           max_digits=3,
                                      #                           decimal_places=0)
                                      )
    mask_octet_2 = forms.DecimalField(label="Mask's octet 2",
                                      # widget=forms.DecimalField(max_value=255,
                                      #                           min_value=0,
                                      #                           max_digits=3,
                                      #                           decimal_places=0)
                                      )
    mask_octet_3 = forms.DecimalField(label="Mask's octet 3",
                                      # widget=forms.DecimalField(max_value=255,
                                      #                           min_value=0,
                                      #                           max_digits=3,
                                      #                           decimal_places=0)
                                      )
    mask_octet_4 = forms.DecimalField(label="Mask's octet 4",
                                      # widget=forms.DecimalField(max_value=255,
                                      #                           min_value=0,
                                      #                           max_digits=3,
                                      #                           decimal_places=0)
                                      )

    class Meta:
        nazwa = forms.CharField(label='',
            widget=forms.TextInput(attrs={"placeholder": "Wpisz nazwę"}))  # etykieta Nazwa się nie pojawi bo label=''
        model = HostAndMask
        fields = [
            'host_octet_1',
            'host_octet_2',
            'host_octet_3',
            'host_octet_4',
            'mask_octet_1',
            'mask_octet_2',
            'mask_octet_3',
            'mask_octet_4'
        ]