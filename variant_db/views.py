from django.shortcuts import render
from .forms import ManualUploadForm
from .models import *
import datetime


# Create your views here.
def home(request):
    return render(request, 'variant_db/home.html', {})


def view(request):
    return render(request, 'variant_db/view.html', {})


def manual_import(request):
    import_form = ManualUploadForm()
    context = {'import_form': import_form,}

    if request.method == 'POST':

        import_form = ManualUploadForm(request.POST)
        if import_form.is_valid:
            print(import_form)
            cleaned_data = import_form.cleaned_data

            # make new family ID - TODO link samples that are related
            family = Family.objects.create()

            # get patient
            patient, created = Patient.objects.get_or_create(
                first_name = cleaned_data['first_name'],
                surname = cleaned_data['surname'],
                proband = True,
                family_id = family
            )

            # TODO get sypmtoms
            
            # make new sample
            sample = dnaSample.objects.create(
                patient_id = patient,
                date_received = datetime.datetime.now(),
                sample_type = 'germline'
            )

            # get test
            test = Test.objects.create(
                sample_id = sample,
                test_type = cleaned_data['test_type'],
                test_date = datetime.datetime.now(),
                sequencer = cleaned_data['sequencer']
            )

            # get variants
            gene = Gene.objects.get(gene_name = 'BRCA1')
            variant, created = Variant.objects.get_or_create(
                test_id = test,
                gene_id = gene,
                coords_cdna = cleaned_data['variant_cdna'],
                coords_protein = cleaned_data['variant_protein'],
                coords_genomic = cleaned_data['variant_genomic']
            )

            # get classification
            classification = Classification.objects.create(
                variant_id = variant,
                classification = cleaned_data['variant_classification']
            )

            # get codes that are true, make evidence object for each one
            code_list = [
                'pvs1', 'ps1', 'ps2', 'ps3', 'ps4', 'pm1', 'pm2', 'pm3',
                'pm4', 'pm5', 'pm6', 'pp1', 'pp2', 'pp3', 'pp4', 'pp5',
                'ba1', 'bs1', 'bs2', 'bs3', 'bs4', 'bp1', 'bp2', 'bp3',
                'bp4', 'bp5', 'bp6'
            ]
            for code in code_list:
                if cleaned_data[code] == True:
                    Evidence.objects.create(
                        classification_id = classification,
                        code_id = acmgCodes.objects.get(code_id=code)
                    )

    return render(request, 'variant_db/manual_import.html', context)
