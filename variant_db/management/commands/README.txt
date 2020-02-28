# Import ACMG codes
python manage.py acmg_importer --filename ~/moka2/variant_db/management/commands/acmg_codes.txt

# Import tets data
python manage.py csv_importer --filename '~Desktop/BRCA1spreadsheet.txt'

# Import gene data
python manage.py coding_gene_importer --filename ~/moka2/variant_db/management/commands/gene_with_protein_product.txt