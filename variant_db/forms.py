from django import forms
from .models import  Patient


class ManualUploadForm(forms.Form):
    """
    """

    first_name = forms.CharField()
    surname = forms.CharField()


