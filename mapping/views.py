from django.shortcuts import render, redirect, reverse
from .models import Full_table
from django.http import HttpResponseRedirect
import csv

# Create your views here.
def handling_file(csv_file):
    file_data = csv_file.read().decode("utf-8")
    file_data = file_data.upper()
    file_data = file_data.split(',')
    error=[]
    for i,j in enumerate(file_data):
        file_data[i]=j.strip()
        if Full_table.objects.filter(alias=file_data[i]).exists():
            print('name')
        elif Full_table.objects.filter(feture_name=file_data[i]).exists():
            print('id')
        else:
            print(file_data[i])
            if file_data[i] not in error:
                error.append(file_data[i])
        while True:
            if '' in error:
                error.remove('')
            else:
                break
    return file_data, error


def home_view(request):
    if request.method == 'POST':
        csv_file = request.FILES['file']
        file_data, error = handling_file(csv_file)
        ids = Full_table.objects.filter(alias__in=file_data)
        return render(request, 'mapping/home.html', {'ids':ids ,'errors': error})
    else:
        ids = None
        error = None
        return render(request,'mapping/home.html',{'ids':ids ,'errors':error})

def mapping_list(request):
    ids = Full_table.objects.all()
    return render(request,'mapping/list.html',{'ids':ids})
