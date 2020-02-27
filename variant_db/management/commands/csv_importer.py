from django.core.management.base import BaseCommand, CommandError
import pandas as pd
from variant_db.models import *

# TODO Remove hardcoded value and allow the user to select the file for upload
# imported_df = pd.read_table('/home/graeme/Desktop/BRCA1 spreadsheet.txt', delimiter='\t')


# utils.utils import csv_importer

class Command(BaseCommand):
    help = 'Import Data from tab-delimited Spreadsheet'
    def add_arguments(self, parser):
        parser.add_argument('--filename', type=str)

    def handle(self, *args, **kwargs):
        filename = kwargs['filename']  # Test data @ '/home/graeme/Desktop/BRCA1 spreadsheet.txt'

        # Import data from tab delimited file
        imported_df = pd.read_table(filename, delimiter='\t')

        # Clean up imported data
        # Clean up 'Name' column
        imported_df['Name'] = imported_df['Name'].str.strip()  # Strip whitespace
        # new data frame with split value columns
        temp_df = imported_df["Name"].str.split(" ", n=1, expand=True)
        # making separate first name column from new data frame
        imported_df["FirstName"] = temp_df[0]
        # making separate last name column from new data frame
        imported_df["LastName"] = temp_df[1]
        # Drop old Name columns
        imported_df.drop(columns=["Name"], inplace=True)

        # Convert "proband" to Boolean value
        imported_df = imported_df.replace(to_replace="Y", value=True)
        imported_df = imported_df.replace(to_replace="N", value=False)
        # TODO - check whether forcing "nan" to True is correct
        imported_df["Proband"].fillna(False, inplace=True)
        # TODO - check whether forcing "nan" to value is correct
        imported_df["Evidence Codes"].fillna("NA", inplace=True)
        # TODO Parse/Remove non-existing PP6 evidence code


        # TODO validate imported variants using variant validator

        # Convert pandas dataframe to dictionary of records to reiterate over
        df_records = imported_df.to_dict('records')

        for record in df_records:

            family, created = Family.objects.get_or_create()

            patient, created = Patient.objects.get_or_create(
                proband=record['Proband'],
                first_name=record['FirstName'],
                last_name=record['LastName'],
                family_id=family,   # No data in spreadsheet linking families
            )

            dnasample, created = dnaSample.objects.get_or_create(
                patient_id=patient,
                date_received="1900-01-01",
                sample_type=record['Description'],
            )

            test, created = Test.objects.get_or_create(
                sample_id=dnasample,
                test_type="",
                test_date="1900-01-01",
                sequencer=record['Sequencer'].strip(),
            )

            variant, created = Variant.objects.get_or_create(
                test_id=test,
                gene_id=Gene.objects.get(gene_name="BRCA1"),
                coords_cdna=record['Variant cDNA'],
                coords_protein=record['Variant Protein'],
                coords_genomic=record['Variant Genome'],
            )

            classification, created = Classification.objects.get_or_create(
                variant_id=variant,
                classification=record['Pathogenicity Code'],
            )

            for code in record['Evidence Codes'].split(","):
                print(code)
                evidence, created = Evidence.objects.get_or_create(
                    classification_id=classification,
                    code_id=acmgCodes.objects.get(code_id=code),
            )


