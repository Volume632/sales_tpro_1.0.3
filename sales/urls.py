
from django.contrib import admin
from django.urls import path
from sales import views  # Import views from the sales app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('abc-xyz-analysis/', views.abc_xyz_analysis, name='abc_xyz_analysis'),
    path('export-forecast/', views.export_forecast, name='export_forecast'),
    path('upload-sales/', views.upload_sales, name='upload_sales'),  # URL for uploading sales data
    path('upload-stock/', views.upload_stock, name='upload_stock'),  # URL for uploading stock data
    path('upload-supplier/', views.upload_supplier, name='upload_supplier'),  # URL for uploading supplier data
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('upload-sales/', views.upload_sales_file, name='upload_sales_file'),
    path('upload-stock/', views.upload_stock_file, name='upload_stock_file'),
    path('upload-supplier/', views.upload_supplier_file, name='upload_supplier_file'),
]