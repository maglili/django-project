from django.shortcuts import render, redirect, reverse
from .models import Full_table, ID_table
from django.http import HttpResponseRedirect
import pandas as pd
from itertools import chain

# Create your views here.
def handling_file(file):
    try:
        df = pd.read_excel(file,squeeze=True,header=None)
    except:
        print('error')
        data_list =None
        errors = None
        return data_list, errors
    data_list = df.tolist()
    data_list_o = data_list.copy()
    errors=[]
    for i,j in enumerate(data_list):
        data_list[i]= j.upper()
        if not ((Full_table.objects.filter(alias=data_list[i]).exists()) or (ID_table.objects.filter(feture_name=data_list[i]).exists())):
            if data_list_o[i] not in errors:
                errors.append(data_list_o[i])
    return data_list, errors


def home_view(request):
    if request.method == 'POST':
        try:
            file = request.FILES['file']
        except:
            return redirect(reverse('mapping:error')) # 防呆
        data_list, errors = handling_file(file)
        if (data_list is None )and (errors is None):
            return redirect(reverse('mapping:error'))  # 防呆
        ids1 = Full_table.objects.filter(alias__in=data_list)
        ids2 = ID_table.objects.filter(feture_name__in=data_list)
        ids = list(chain(ids1, ids2))
        return render(request, 'mapping/home.html', {'ids':ids ,'errors': errors})
    else:
        ids = None
        error = None
        return render(request,'mapping/home.html',{'ids':ids ,'errors':error})

def mapping_list(request):
    ids = Full_table.objects.all()
    return render(request,'mapping/list.html',{'ids':ids})

def page_error(request):
    return render(request,'mapping/error.html',{})
