
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('abc-xyz-analysis/', views.abc_xyz_analysis, name='abc_xyz_analysis'),  # Страница анализа ABC-XYZ
    path('export-forecast/', views.export_forecast, name='export_forecast'),  # Страница экспорта прогноза
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register', views.register_view, name='register'),
    path('upload-products/', views.upload_product_file, name='upload_product_file'),
]