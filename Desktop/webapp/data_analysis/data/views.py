from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .forms import FileForm
import pandas as pd
from .visualization import plot
from .list_files import files_and_columns
from django.views.decorators.csrf import csrf_exempt
from .models import CsvData
from . compute import computation
import threading 
from .database_operations import inserting
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'data/home.html'

    

def upload_file(request):
    form = FileForm()
    context = {'form':form}
    label = False # to check if the uploaded file already exists or not  

    with open("data/static/media/files_list.txt", 'r') as filename:
        context['uploaded_files'] = filename.readlines()

    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        uploaded_file = request.FILES['file']

        #to chekc the files is CSV or not and existing file or not
        if uploaded_file.name.endswith('.csv') and uploaded_file.name+'\n' not in context['uploaded_files']:
            with open("data/static/media/files_list.txt", 'a') as filename:
                filename.writelines([uploaded_file.name])
                filename.write('\n')

        
            with open(uploaded_file.name, 'wb+') as destination:  
                for chunk in uploaded_file.chunks():  
                    destination.write(chunk)
              
            inserted = inserting(uploaded_file)
            if inserted:
                context['alert'] = "File Uploaded successfully"
                with open("data/static/media/files_list.txt", 'r') as filename:
                    context['uploaded_files'] = filename.readlines()
                return render(request, 'data/store.html',context)
        else:
            context['alert'] = "File already Uploaded successfully or Wrong File Choosen."
            return render(request, 'data/store.html',context)
        
    
    return render(request, 'data/store.html',context)

@csrf_exempt
def analyze(request):
    
    #getting files and columns exist in the database.
    context = files_and_columns()
    context['computedval'] = ''

    if request.method == 'POST':
        operation = request.POST.get('operation')
        file = request.POST.get('file')
        column = request.POST.get('columns')
        val = computation(operation =operation, file = file, column = column)
        context['computedval'] = val 
        return render(request, 'data/visualize.html', context)
      
    elif request.method == 'GET' :
        column2 = request.GET.get('column2')
        file = request.GET.get('file')
        column1 = request.GET.get('column1')
        #generate plot and show it to the screen
        path = plot(file = file, column1=column1, column2=column2)
        print(path)
        context['path'] =path
        
    return render(request, 'data/visualize.html', context)