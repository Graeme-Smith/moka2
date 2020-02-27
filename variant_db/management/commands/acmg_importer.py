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
        filename = kwargs['filename']  # acmg_codes.txt

        # Import data from tab delimited file
        imported_df = pd.read_table(filename, delimiter='\t')


        # Convert pandas dataframe to dictionary of records to reiterate over
        df_records = imported_df.to_dict('records')

        for record in df_records:
                acmgcodes, created = acmgCodes.objects.get_or_create(
                    code_id=record['code_id'],
                    description=record['description']
            )


