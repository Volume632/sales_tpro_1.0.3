import pandas as pd
from .models import SalesRecord

def process_file(df):
    """
    Обрабатывает DataFrame и сохраняет данные в базу данных.
    df: pandas DataFrame
    """
    for _, row in df.iterrows():
        # Предположим, что у вас есть следующие столбцы в DataFrame: 'Период', 'id', 'наименование', 'количество'
        period = row['Период']
        product_id = row['id']
        name = row['наименование']
        quantity = row['количество']
        
        # Преобразуйте период в год
        year = period.split('-')[0]  # Например, '2021-01' => '2021'
        
        # Сохранение в базу данных
        SalesRecord.objects.update_or_create(
            period=year,
            product_id=product_id,
            defaults={'name': name, 'quantity': quantity}
        )