import pandas as pd
from django.core.management.base import BaseCommand
from sales.models import Product

class Command(BaseCommand):
    help = 'Load stock data from an Excel file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        df = pd.read_excel(file_path)

        for index, row in df.iterrows():
            product, created = Product.objects.get_or_create(id=row['id'], defaults={'name': row['name']})
            product.quantity = row['quantity']
            product.save()
        self.stdout.write(self.style.SUCCESS('Successfully loaded stock data'))