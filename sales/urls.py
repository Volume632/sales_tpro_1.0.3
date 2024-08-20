from django.urls import path
from . import views

urlpatterns = [
    path('export_forecast/', views.export_forecast, name='export_forecast'),
]