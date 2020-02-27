from django.shortcuts import render
from .forms import ManualUploadForm

# Create your views here.
def home(request):
    return render(request, 'variant_db/home.html', {})


def view(request):
    return render(request, 'variant_db/view.html', {})


def manual_import(request):
    import_form = ManualUploadForm()

    context = {'import_form': import_form,}
    return render(request, 'variant_db/manual_import.html', context)
