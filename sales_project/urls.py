from django.contrib import admin
from django.urls import include, path
from sales import views  # Убедитесь, что views импортирован

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Корневой маршрут
    path('upload/', include('sales.urls')),  # Подключение маршрутов из приложения sales
]