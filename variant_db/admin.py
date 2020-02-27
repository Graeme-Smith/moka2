from django.contrib import admin
from .models import *


class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
admin.site.register(Patient, PatientAdmin)

admin.site.register(Family)

class PhenotypeAdmin(admin.ModelAdmin):
    list_display = ('visit_id', 'visit_date', 'patient_id', 'description', 'stage')
admin.site.register(Phenotype, PhenotypeAdmin)

class dnaSampleAdmin(admin.ModelAdmin):
    list_display = ('sample_id', 'patient_id')
admin.site.register(dnaSample, dnaSampleAdmin)

class TestAdmin(admin.ModelAdmin):
    list_display = ('test_id', 'test_type')
admin.site.register(Test, TestAdmin)

class VariantAdmin(admin.ModelAdmin):
    list_display = ('variant_id', 'coords_cdna', 'coords_protein', 'coords_genomic')
admin.site.register(Variant, VariantAdmin)

class GeneAdmin(admin.ModelAdmin):
    list_display = ('gene_id', 'gene_name')
admin.site.register(Gene, GeneAdmin)

class ClassificationAdmin(admin.ModelAdmin):
    list_display = ('classification_id', 'variant_id', 'classification')
admin.site.register(Classification, ClassificationAdmin)

class EvidenceAdmin(admin.ModelAdmin):
    list_display = ('evidence_id', 'classification_id', 'code_id')
admin.site.register(Evidence), EvidenceAdmin

class acmgCodesAdmin(admin.ModelAdmin):
    list_display = ('code_id', 'description')
admin.site.register(acmgCodes, acmgCodesAdmin)
