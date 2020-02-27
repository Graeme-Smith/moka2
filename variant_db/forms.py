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
    stage = forms.ChoiceField(choices=(('1' 'I'), ('2', 'II'), ('3', 'III'), ('4', 'IV')))
    test_type = forms.ChoiceField(choices=(
        ('NGS_WES', 'NGS Whole Exome Sequencing'),
        ('NGS_WGS', 'NGS Whole Genome Sequencing'),
        ('NGS_panel', 'NGS targetted panel'))
    )
    sequencer = forms.ChoiceField(choices=(
        ('HiSeq', 'HiSeq'),
        ('MiSeq', 'MiSeq'),
        ('NovaSeq', 'NovaSeq'))
    )
    variant_cdna = forms.CharField()
    variant_protein = forms.CharField()
    variant_genomic = forms.CharField()
    variant_classification = forms.ChoiceField(choices=(
            ('1', 'Benign'),
            ('2', 'Likely Benign'),
            ('3', 'VUS'),
            ('4', 'Likely Pathogenic'),
            ('5', 'Pathogenic'))
    )

    #pathogenic codes
    pvs1 = forms.BooleanField(required=False)
    ps1 = forms.BooleanField(required=False)
    ps2 = forms.BooleanField(required=False)
    ps3 = forms.BooleanField(required=False)
    ps4 = forms.BooleanField(required=False)
    pm1 = forms.BooleanField(required=False)
    pm2 = forms.BooleanField(required=False)
    pm3 = forms.BooleanField(required=False)
    pm4 = forms.BooleanField(required=False)
    pm5 = forms.BooleanField(required=False)
    pm6 = forms.BooleanField(required=False)
    pp1 = forms.BooleanField(required=False)
    pp2 = forms.BooleanField(required=False)
    pp3 = forms.BooleanField(required=False)
    pp4 = forms.BooleanField(required=False)
    pp5 = forms.BooleanField(required=False)

    #benign codes
    ba1 = forms.BooleanField(required=False)
    bs1 = forms.BooleanField(required=False)
    bs2 = forms.BooleanField(required=False)
    bs3 = forms.BooleanField(required=False)
    bs4 = forms.BooleanField(required=False)
    bp1 = forms.BooleanField(required=False)
    bp2 = forms.BooleanField(required=False)
    bp3 = forms.BooleanField(required=False)
    bp4 = forms.BooleanField(required=False)
    bp5 = forms.BooleanField(required=False)
    bp6 = forms.BooleanField(required=False)

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
            Field('first_name', placeholder="Enter patient's first name"),
            Field('surname', placeholder="Enter patient's surname"),
            HTML('<br><h5>Patient phenotype</h5>'),
            Field('description', placeholder="Enter a description of the patient's symptoms"),
            Field('stage'),
            HTML('<br><h5>Test information</h5>'),
            Field('test_type'),
            Field('sequencer'),
            HTML('<br><h5>Variant information</h5>'),
            Field('variant_cdna', placeholder="Enter cDNA co-ordinates in this format: c.303T>G"),
            Field('variant_protein', placeholder="Enter protein co-ordinates in this format: p.(Tyr101*)"),
            Field('variant_genomic', placeholder="Enter genomic DNA co-ordinates in this format: g.41256277A>C"),
            Field('variant_classification'),
            HTML('<br><h5>Pathogenic ACMG codes</h5>'),
            Field('pvs1'),
            Field('ps1'),
            Field('ps2'),
            Field('ps3'),
            Field('ps4'),
            Field('pm1'),
            Field('pm2'),
            Field('pm3'),
            Field('pm4'),
            Field('pm5'),
            Field('pm6'),
            Field('pp1'),
            Field('pp2'),
            Field('pp3'),
            Field('pp4'),
            Field('pp5'),
            HTML('<br><h5>Benign ACMG codes</h5>'),
            Field('ba1'),
            Field('bs1'),
            Field('bs2'),
            Field('bs3'),
            Field('bs4'),
            Field('bp1'),
            Field('bp2'),
            Field('bp3'),
            Field('bp4'),
            Field('bp5'),
            Field('bp6'),
        )
        # change labels on some fields
        self.fields['variant_cdna'].label = 'cDNA co-ordinates'
        self.fields['variant_protein'].label = 'Protein co-ordinates'
        self.fields['variant_genomic'].label = 'Genomic DNA co-ordinates'
        self.fields['pvs1'].label = 'PVS1'
        self.fields['ps1'].label = 'PS1'
        self.fields['ps2'].label = 'PS2'
        self.fields['ps3'].label = 'PS3'
        self.fields['ps4'].label = 'PS4'
        self.fields['pm1'].label = 'PM1'
        self.fields['pm2'].label = 'PM2'
        self.fields['pm3'].label = 'PM3'
        self.fields['pm4'].label = 'PM4'
        self.fields['pm5'].label = 'PM5'
        self.fields['pm6'].label = 'PM6'
        self.fields['pp1'].label = 'PP1'
        self.fields['pp2'].label = 'PP2'
        self.fields['pp3'].label = 'PP3'
        self.fields['pp4'].label = 'PP4'
        self.fields['pp5'].label = 'PP5'
        self.fields['ba1'].label = 'BA1'
        self.fields['bs1'].label = 'BS1'
        self.fields['bs2'].label = 'BS2'
        self.fields['bs3'].label = 'BS3'
        self.fields['bs4'].label = 'BS4'
        self.fields['bp1'].label = 'BP1'
        self.fields['bp2'].label = 'BP2'
        self.fields['bp3'].label = 'BP3'
        self.fields['bp4'].label = 'BP4'
        self.fields['bp5'].label = 'BP5'
        self.fields['bp6'].label = 'BP6'
