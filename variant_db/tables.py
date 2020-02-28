import django_tables2 as tables
from .models import Patient
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

class PatientTable(tables.Table):
    class Meta:
        model = Patient
        template_name = "django_tables2/bootstrap.html"
        fields = ("patient_id", "first_name", "last_name", "proband", )
        DJANGO_TABLES2_TEMPLATE = "django_tables2/bootstrap4.html"

class FilteredPatientListView(SingleTableMixin, FilterView):
    table_class = PatientTable
    model = Patient
    template_name = "view.html"

    filterset_class = Patient
