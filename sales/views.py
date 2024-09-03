from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SalesFileForm, SupplierFileForm, ProductFileForm
from .models import SalesRecord, Product, Supplier
from .utils import import_sales_data, import_stock_data, import_supplier_data

def home(request):
    return render(request, 'home.html')

def upload_sales_file(request):
    if request.method == 'POST':
        form = SalesFileForm(request.POST, request.FILES)
        if form.is_valid():
            sales_file = form.save()
            import_sales_data(sales_file.file.path)
            messages.success(request, 'Sales data uploaded and processed successfully!')
            return redirect('home')
    else:
        form = SalesFileForm()
    return render(request, 'sales/upload_sales.html', {'form': form})

def upload_stock_file(request):
    if request.method == 'POST':
        form = ProductFileForm(request.POST, request.FILES)
        if form.is_valid():
            stock_file = form.cleaned_data['file']
            import_stock_data(stock_file.temporary_file_path())
            messages.success(request, 'Stock data uploaded successfully!')
            return redirect('home')
    else:
        form = ProductFileForm()
    return render(request, 'sales/upload_stock.html', {'form': form})

def upload_supplier_file(request):
    if request.method == 'POST':
        form = SupplierFileForm(request.POST, request.FILES)
        if form.is_valid():
            supplier_file = form.save()
            import_supplier_data(supplier_file.file.path)
            messages.success(request, 'Supplier data uploaded successfully!')
            return redirect('home')
    else:
        form = SupplierFileForm()
    return render(request, 'sales/upload_supplier.html', {'form': form})