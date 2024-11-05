# forms.py
from django import forms
from .models import Recepit


class RecepitForm(forms.ModelForm):
    class Meta:
        model = Recepit
        fields = '__all__'
