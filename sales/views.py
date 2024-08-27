from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import pandas as pd
from .utils import process_file  # Допустим, у вас есть функция для обработки файла
from django.http import HttpResponse
from io import BytesIO
from .analysis import perform_abc_xyz_analysis
from django.shortcuts import get_object_or_404  # Импортируем необходимые функции из Django.
from .models import SalesRecord, Product, Supplier  # Импортируем модели, которые нам нужны для работы с данными.
from .models import Forecast  # Импорт модели
from django.contrib.auth.decorators import login_required
from .forms import SalesFileForm, SupplierFileForm
from .models import SalesFile, SupplierFile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import ProductFileForm

# Функция для входа
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid credentials'})
    return render(request, 'registration/login.html')

# Функция для выхода
def logout_view(request):
    logout(request)
    return redirect('home')

# Функция для регистрации
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Представление для главной страницы
@login_required
def home(request):
    """
    Функция для отображения главной страницы.
    """
    # Получаем все записи о продажах, продуктах и поставщиках из базы данных.
    sales_records = SalesRecord.objects.all()
    products = Product.objects.all()
    suppliers = Supplier.objects.all()

    # Передаем данные в шаблон для отображения.
    context = {
        'sales_records': sales_records,
        'products': products,
        'suppliers': suppliers,
    }
    return render(request, 'sales/home.html', context)

# Представление для отображения деталей конкретного продукта
@login_required
def product_detail(request, product_id):
    """
    Функция для отображения страницы с информацией о конкретном продукте.
    """
    # Получаем объект продукта по его ID или возвращаем 404, если продукт не найден.
    product = get_object_or_404(Product, id=product_id)
    
    # Передаем данные о продукте в шаблон.
    context = {
        'product': product,
    }
    return render(request, 'sales/product_detail.html', context)

# Представление для загрузки файла (например, с данными о продажах)
@login_required
def upload_file(request):
    """
    Функция для обработки загрузки файла.
    """
    if request.method == 'POST':
        # Если метод запроса POST, то обрабатываем файл
        uploaded_file = request.FILES['file']
        
        # Процесс обработки файла (функция process_file будет реализована в utils.py)
        process_file(uploaded_file)
        
        # После обработки перенаправляем пользователя на страницу успеха.
        return render(request, 'sales/upload_success.html')

    # Если метод запроса GET, просто отображаем страницу загрузки файла.
    return render(request, 'sales/upload.html')

# Представление для выполнения анализа ABC/XYZ
@login_required
def abc_xyz_analysis(request):
    """
    Функция для выполнения анализа ABC/XYZ.
    """
    # Выполняем анализ с использованием функции из analysis.py
    analysis_result = perform_abc_xyz_analysis()

    # Передаем результат анализа в шаблон для отображения.
    context = {
        'analysis_result': analysis_result,
    }
    return render(request, 'sales/abc_xyz_analysis.html', context)

@login_required
def get_forecast_data():
    # Получение данных из модели
    forecasts = Forecast.objects.all()  # Замените на вашу логику получения данных

    # Преобразование данных в DataFrame
    data = pd.DataFrame(list(forecasts.values('field1', 'field2', 'field3')))  # Замените на ваши поля
    return data
@login_required
def export_forecast(request):
    # Получение данных для экспорта
    forecast_data = get_forecast_data()  # Функция для получения данных

    # Создание Excel-файла
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    forecast_data.to_excel(writer, sheet_name='Forecast', index=False)
    writer.save()
    output.seek(0)

    # Возвращение файла пользователю
    response = HttpResponse(output, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=forecast.xlsx'
    return response

import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProductFileForm
from .models import Product

def upload_product_file(request):
    if request.method == 'POST':
        form = ProductFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            try:
                # Чтение файла Excel в DataFrame
                df = pd.read_excel(file, engine='openpyxl')

                # Опционально: Проверьте, что DataFrame имеет нужные столбцы
                if not {'name', 'price'}.issubset(df.columns):
                    messages.error(request, 'Файл должен содержать столбцы: name и price.')
                    return redirect('upload_product_file')

                # Сохранение данных в модель Product
                for _, row in df.iterrows():
                    Product.objects.create(
                        name=row['name'],
                        price=row['price']
                    )

                messages.success(request, 'Продукты успешно загружены.')
                return redirect('home')  # Перенаправление на домашнюю страницу или другую
            except Exception as e:
                messages.error(request, f'Ошибка при загрузке файла: {e}')
                return redirect('upload_product_file')
    else:
        form = ProductFileForm()

    return render(request, 'sales/upload_product_file.html', {'form': form})