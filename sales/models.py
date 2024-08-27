from django.db import models

# Модель для продуктов
class Product(models.Model):
    # Поле для хранения идентификатора продукта (генерируется автоматически как Primary Key)
    id = models.AutoField(primary_key=True)
    
    # Поле для хранения имени продукта
    name = models.CharField(max_length=255, unique=True)  # Уникальное имя продукта, длина до 255 символов
    
    # Поле для хранения цены продукта
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена продукта с двумя десятичными знаками
    
    # Поле для хранения даты и времени добавления продукта
    created_at = models.DateTimeField(auto_now_add=True)  # Автоматически устанавливается при создании записи
    
    # Строковое представление модели
    def __str__(self):
        return self.name

# Модель для записей о продажах
class SalesRecord(models.Model):
    # Поле для хранения идентификатора записи о продаже (генерируется автоматически как Primary Key)
    id = models.AutoField(primary_key=True)
    
    # Поле для хранения периода (например, года) продажи
    period = models.CharField(max_length=20)  # Период, например, "2021", "2022"
    
    # Связь с продуктом через ForeignKey
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Удаление продукта приведет к удалению всех связанных продаж
    
    # Поле для хранения количества проданного товара
    quantity = models.IntegerField()  # Целое число, количество проданных товаров
    
    # Поле для хранения даты и времени добавления записи
    created_at = models.DateTimeField(auto_now_add=True)  # Автоматически устанавливается при создании записи
    
    # Строковое представление модели
    def __str__(self):
        return f"{self.product.name} - {self.period}"

# Модель для поставщиков
class Supplier(models.Model):
    # Поле для хранения идентификатора поставщика (генерируется автоматически как Primary Key)
    id = models.AutoField(primary_key=True)
    
    # Поле для хранения имени поставщика
    name = models.CharField(max_length=255, unique=True)  # Уникальное имя поставщика, длина до 255 символов
    
    # Поле для хранения контактной информации
    contact_info = models.TextField()  # Текстовое поле для хранения контактной информации
    
    # Поле для хранения даты и времени добавления поставщика
    created_at = models.DateTimeField(auto_now_add=True)  # Автоматически устанавливается при создании записи
    
    # Строковое представление модели
    def __str__(self):
        return self.name
    
class Forecast(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
    field3 = models.DateField()
    # Добавьте необходимые поля

class SalesFile(models.Model):
    file = models.FileField(upload_to='sales_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sales File: {self.file.name}"

class SupplierFile(models.Model):
    file = models.FileField(upload_to='supplier_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Supplier File: {self.file.name}"
