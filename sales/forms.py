from django import forms
from .models import SalesFile, SupplierFile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Импорт модели User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
        
class SalesFileForm(forms.ModelForm):
    class Meta:
        model = SalesFile
        fields = ['file']

class SupplierFileForm(forms.ModelForm):
    class Meta:
        model = SupplierFile
        fields = ['file']
        
        
class ProductFileForm(forms.Form):
    file = forms.FileField(label='Выберите файл Excel')