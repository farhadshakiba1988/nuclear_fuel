# forms.py
from django import forms
from .models import Person, UploadedFile


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


# forms.py
from django import forms
from .models import UploadedFile


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            # بررسی نوع فایل برای txt و excel
            if not (file.name.endswith('.txt') or file.name.endswith('.xls') or file.name.endswith('.xlsx')):
                raise forms.ValidationError("Only .txt, .xls, and .xlsx files are allowed.")
        return file
