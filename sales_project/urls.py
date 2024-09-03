from django.contrib import admin
from django.urls import path, include
from sales import views  # Импортируйте views из sales

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sales.urls')),  # Подключение маршрутов из приложения sales
    path('accounts/', include('django.contrib.auth.urls')),  # Включение URL для аутентификации
    path('', views.home, name='home'),
    path('export-forecast/', views.export_forecast, name='export_forecast'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]
