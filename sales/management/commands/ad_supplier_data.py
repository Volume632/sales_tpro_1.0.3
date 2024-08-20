import pandas as pd
from django.core.management.base import BaseCommand
from sales.models import Supplier

class Command(BaseCommand):
    help = 'Load supplier data from an Excel file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        df = pd.read_excel(file_path)

        for index, row in df.iterrows():
            Supplier.objects.update_or_create(
                id=row['id'],
                defaults={'name': row['name'], 'price': row['price']}
            )
        self.stdout.write(self.style.SUCCESS('Successfully loaded supplier data'))