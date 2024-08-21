from django.shortcuts import render
from .forms import UploadFileForm
import pandas as pd

def home(request):
    return render(request, 'sales/home.html')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_excel(file)
            # Обработка данных
            return render(request, 'sales/upload_success.html')
    else:
        form = UploadFileForm()
    return render(request, 'sales/upload.html', {'form': form})