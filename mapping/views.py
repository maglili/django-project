from django.shortcuts import render, redirect
from .models import Full_table
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
import csv

# Create your views here.
def home_view(request):
    if request.method == 'POST':
        csv_file = request.FILES['file']
        file_data = csv_file.read().decode("utf-8")
        file_data = file_data.upper()
        file_data = file_data.split(',')
        for i,j in enumerate(file_data):
            file_data[i]=j.strip()
        print(file_data)
        ids = Full_table.objects.filter(alias__in=file_data)
        return render(request,'mapping/home.html',{'ids':ids})

    else:
        ids = Full_table.objects.all()[:3]
        return render(request,'mapping/home.html',{'ids':ids})
