from django.db import models


class Patient(models.Model):
    """
    Model to store patient details
    """
    patient_id = models.AutoField(primary_key=True)
    family_id = models.ForeignKey('Family', on_delete=models.CASCADE)
    proband = models.BooleanField()
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_phenotype(self):
        return Phenotype.objects.get(patient_id=self.patient_id)


class Family(models.Model):
    """
    Model to store family details
    """
    family_id = models.AutoField(primary_key=True)


class Phenotype(models.Model):
    """
    Model to store the patient symptoms at a particular clinic visit
    """
    visit_id = models.AutoField(primary_key=True)
    visit_date = models.DateField()
    patient_id = models.ForeignKey('Patient', on_delete=models.CASCADE)
    description = models.TextField()
    stage = models.CharField(max_length=3, choices=(('1', 'I'), ('2', 'II'), ('3', 'III'), ('4', 'IV')))

    def __str__(self):
        return self.description


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

    def __str__(self):
        return self.coords_genomic
    
    def get_classification(self):
        classification = Classification.objects.get(variant_id=self.variant_id)
        return str(classification)

class Gene(models.Model):
    """
    Model to store models details
    """
    # HGNC gene ID
    gene_id = models.CharField(max_length=15, primary_key=True)
    # HGNC approved symbol
    gene_name = models.CharField(max_length=20)
    # TODO - Add gene alias symbols

    def __str__(self):
        return self.gene_name


class Classification(models.Model):
    """
    Model to store variant classification details
    """
    CODES=(('1', 'Benign'),
           ('2', 'Likely Benign'),
           ('3', 'VUS'),
           ('4', 'Likely Pathogenic'),
           ('5', 'Pathogenic'))
    classification_id = models.AutoField(primary_key=True)
    variant_id = models.ForeignKey('Variant', on_delete=models.CASCADE)
    classification = models.CharField(max_length=10, choices=CODES)

    def __str__(self):
        """
        Get the classification and look up code number in codes list
        """
        classification = self.classification
        for c_num, c_desc in self.CODES:
            if classification == c_num:
                classification = c_desc
        return classification


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
    code_id = models.CharField(max_length=4, primary_key=True)
    description = models.TextField()
