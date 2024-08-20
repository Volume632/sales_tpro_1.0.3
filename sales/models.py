from django.db import models

class Supplier(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
   

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class Sales(models.Model):
    month_year = models.CharField(max_length=7)  # Формат: YYYY-MM
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_sold = models.IntegerField()

    def __str__(self):
        return f"{self.product.name} - {self.month_year}"