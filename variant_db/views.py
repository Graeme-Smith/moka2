from django.shortcuts import render
from .forms import ManualUploadForm
from .models import *
import datetime


def home(request):
    total_classifications = Classification.objects.all()

    num_classification = {
        'num_total': len(total_classifications),
        'num_b': len(total_classifications.filter(classification='1')),
        'num_lb': len(total_classifications.filter(classification='2')),
        'num_vus': len(total_classifications.filter(classification='3')),
        'num_lp': len(total_classifications.filter(classification='4')),
        'num_p': len(total_classifications.filter(classification='5'))
    }

    return render(request, 'variant_db/home.html', {'counts': num_classification})


def view(request):
    """
    View a list of variants
    """
    variant_list = Variant.objects.all()

    return render(request, 'variant_db/view.html', {'variants': variant_list})


def manual_import(request):
    """
    Takes the input from the manual input form and imports it into the database
    """
    # setup view
    import_form = ManualUploadForm()
    context = {'import_form': import_form, 'message': None}

    # if form is submitted
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
                last_name = cleaned_data['last_name'],
                proband = True,
                family_id = family
            )

            # make new phenotype entry
            phenotype = Phenotype.objects.create(
                visit_date = datetime.datetime.now(),
                patient_id = patient,
                description = cleaned_data['description'],
                stage = cleaned_data['stage']
            )
            
            # make new sample
            sample = dnaSample.objects.create(
                patient_id = patient,
                date_received = datetime.datetime.now(),
                sample_type = 'germline'
            )

            # make new test
            test = Test.objects.create(
                sample_id = sample,
                test_type = cleaned_data['test_type'],
                test_date = datetime.datetime.now(),
                sequencer = cleaned_data['sequencer']
            )

            # get variants
            gene = Gene.objects.get(gene_id = 'HGNC:1100') # TODO expand to more genes
            variant, created = Variant.objects.get_or_create(
                test_id = test,
                gene_id = gene,
                coords_cdna = cleaned_data['variant_cdna'],
                coords_protein = cleaned_data['variant_protein'],
                coords_genomic = cleaned_data['variant_genomic']
            )

            # make new classification
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
                        code_id = acmgCodes.objects.get(code_id=code.upper())
                    )

            # add success message to page
            context['message'] = ['Variant was uploaded successfully']

    # render the page
    return render(request, 'variant_db/manual_import.html', context)
