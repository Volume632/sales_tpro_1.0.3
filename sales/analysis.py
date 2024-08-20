import pandas as pd
from sales.models import Sales, Product, Supplier

def calculate_abc_xyz():
    sales_data = Sales.objects.all()
    products = Product.objects.all()

    # Пример анализа ABC-XYZ:
    sales_df = pd.DataFrame(list(sales_data.values('product__name', 'quantity_sold')))
    # Дополните логику анализа здесь
    return sales_df

def forecast_sales(product_id, months=2):
    sales = Sales.objects.filter(product_id=product_id)
    # Пример простого прогнозирования (дополните по необходимости)
    forecast = {}
    return forecast