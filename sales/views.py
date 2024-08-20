from django.http import HttpResponse
import pandas as pd
from .analysis import forecast_sales  # Убедитесь, что функция forecast_sales определена

def export_forecast(request):
    product_id = request.GET.get('product_id')
    months = int(request.GET.get('months', 2))
    forecast = forecast_sales(product_id, months)

    df = pd.DataFrame(forecast)
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=forecast.xlsx'
    df.to_excel(response, index=False)
    
    return response