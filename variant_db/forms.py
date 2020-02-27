from django import forms
from .models import  Patient

from django.urls import reverse
from crispy_forms.bootstrap import Field
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, HTML


class ManualUploadForm(forms.Form):
    """
    Form for manually inputting data
    """
    first_name = forms.CharField()
    surname = forms.CharField()
    description = forms.CharField()
    stage = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(ManualUploadForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'manual-upload-form'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('view')
        self.helper.add_input(Submit('submit', 'Import', css_class='btn-success'))
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            HTML('<br><h5>Patient information</h5>'),
            Field('first_name'),
            Field('surname'),
            HTML('<br><h5>Patient phenotype</h5>'),
            Field('description'),
            Field('stage'),
        )
