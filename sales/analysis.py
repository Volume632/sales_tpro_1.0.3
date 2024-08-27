from .models import SalesRecord, Product, Supplier  # Импорт моделей из models.py
import pandas as pd

def perform_abc_xyz_analysis():
    """
    Выполняет анализ ABC/XYZ для всех продуктов в базе данных.
    
    ABC-анализ классифицирует товары на основе их значимости:
    - A: самые важные товары (обычно приносят 70-80% дохода)
    - B: товары средней важности (15-25% дохода)
    - C: наименее важные товары (5-10% дохода)
    
    XYZ-анализ классифицирует товары на основе их стабильности спроса:
    - X: товары с устойчивым спросом
    - Y: товары с умеренной колеблемостью спроса
    - Z: товары с высоким уровнем колеблемости спроса
    
    Возвращает результаты анализа в виде списка словарей, где каждый словарь представляет один продукт.
    """
    
    # Получаем все записи о продажах из базы данных
    sales_records = SalesRecord.objects.all()
    
    # Инициализируем структуру для хранения данных о суммарной выручке и стабильности спроса по каждому продукту
    product_data = {}
    
    for record in sales_records:
        product = record.product
        if product not in product_data:
            product_data[product] = {
                'total_revenue': 0,
                'total_quantity': 0,
                'periods': [],
            }
        
        # Обновляем данные о продукте
        product_data[product]['total_revenue'] += record.revenue
        product_data[product]['total_quantity'] += record.quantity
        product_data[product]['periods'].append(record.period)

    # Рассчитываем классификации ABC и XYZ
    for product, data in product_data.items():
        # ABC анализ основан на общей выручке
        total_revenue = data['total_revenue']
        if total_revenue >= 0.8 * sum([p['total_revenue'] for p in product_data.values()]):
            data['abc_class'] = 'A'
        elif total_revenue >= 0.15 * sum([p['total_revenue'] for p in product_data.values()]):
            data['abc_class'] = 'B'
        else:
            data['abc_class'] = 'C'

        # XYZ анализ основан на стабильности спроса (колебания между периодами)
        periods = data['periods']
        if len(periods) > 1:
            # Простой способ рассчитать коэффициент вариации (как пример)
            average = sum(periods) / len(periods)
            variance = sum((x - average) ** 2 for x in periods) / len(periods)
            stddev = variance ** 0.5
            coefficient_of_variation = stddev / average
            if coefficient_of_variation < 0.1:
                data['xyz_class'] = 'X'
            elif coefficient_of_variation < 0.25:
                data['xyz_class'] = 'Y'
            else:
                data['xyz_class'] = 'Z'
        else:
            data['xyz_class'] = 'Z'

    # Преобразуем результаты в удобный формат
    results = []
    for product, data in product_data.items():
        results.append({
            'product': product,
            'abc_class': data['abc_class'],
            'xyz_class': data['xyz_class'],
            'total_revenue': data['total_revenue'],
            'total_quantity': data['total_quantity'],
        })

    return results