from django import forms
from . import models


class NameForm(forms.Form):
    your_name = forms.CharField(max_length=100, label='Your Name')


class NewForm(forms.ModelForm):
    class Meta:
        model = models.Case
        fields = ['your_name', 'childs_name', 'case_number']
