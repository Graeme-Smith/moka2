from django.db import models


# Create your models here.


class Patient(models.Model):
    """
    Model to store patient details
    """
    patient_id = models.AutoField(primary_key=True)
    family_id = models.ForeignKey('Family', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    proband = models.BooleanField()
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)


class Family(models.Model):
    """
    Model to store family details
    """
    family_id = models.AutoField(primary_key=True)


class dnaSample(models.Model):
    """
    Model to store dnaSample details
    """
    sample_id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey('Patient', on_delete=models.CASCADE)
    date_received = models.DateField()
    sample_type = models.CharField(max_length=10, choices=(('germline', 'germline'), ('somatic', 'somatic')))


class Test(models.Model):
    """
    Model to store test details
    """
    test_id = models.AutoField(primary_key=True)
    sample_id = models.ForeignKey('dnaSample', on_delete=models.CASCADE)
    test_type = models.CharField(max_length=10, choices=(('NGS_WES', 'NGS_WES'),
                                                         ('NGS_WGS', 'NGS_WGS'),
                                                         ('NGS_panel', 'NGS_panel')))
    test_date = models.DateField()
    sequencer = models.CharField(max_length=10, choices=(('HiSeq', 'HiSeq'),
                                                         ('MiSeq', 'MiSeq'),
                                                         ('NovaSeq', 'NovaSeq')))


class Variant(models.Model):
    """
    Model to store variant details
    """
    variant_id = models.AutoField(primary_key=True)
    test_id = models.ForeignKey('test', on_delete=models.CASCADE)
    gene_id = models.ForeignKey('Gene', on_delete=models.CASCADE)
    coords_cdna = models.CharField(max_length=50)
    coords_protein = models.CharField(max_length=50)
    coords_genomic = models.CharField(max_length=50)


class Gene(models.Model):
    """
    Model to store models details
    """
    # HGNC gene ID
    gene_id = models.CharField(max_length=15, primary_key=True)
    # HGNC approved symbol
    gene_name = models.CharField(max_length=20)
    # TODO - Add gene alias symbols


class Classification(models.Model):
    """
    Model to store variant classification details
    """
    classification_id = models.AutoField(primary_key=True)
    variant_id = models.ForeignKey('Variant', on_delete=models.CASCADE)
    classification = models.CharField(max_length=10, choices=(('1', 'Benign'),
                                                              ('2', 'Likely Benign'),
                                                              ('3', 'VUS'),
                                                              ('4', 'Likely Pathogenic'),
                                                              ('5', 'Pathogenic')))


class Evidence(models.Model):
    """
    Model to store classification code details
    """
    evidence_id = models.AutoField(primary_key=True)
    classification_id = models.ForeignKey('Classification', on_delete=models.CASCADE)
    code_id = models.ForeignKey('acmgCodes', on_delete=models.CASCADE)
    # TODO - add user adjustable code strength
    # code_strength


class acmgCodes(models.Model):
    """
    Model to store patient details
    """
    code_id = models.CharField(max_length=4,
                               primary_key=True)
    description = models.TextField()
