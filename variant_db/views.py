# Create your views here.
def home(request):
    return render(request, 'variant_db/home.html', {})


def view(request):
    return render(request, 'variant_db/view.html', {})


def manual_import(request):
    return render(request, 'variant_db/manual_import.html', {})
