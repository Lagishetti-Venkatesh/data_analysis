import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from .models import CsvData
import os
from django.db.models import Q

def plot(file, column1, column2):
    """
    will generate plot object and and save it in static media folder 
    returns the absolute file path.
    """
    if file == None or column1 == None or column2 == None:
        return ''
    file = file.replace(".csv", '').strip()
    column1 = column1.strip()
    column2 = column2.strip()
    print(file, column1, column2)
    c1, c2 = [], []
    Query  = CsvData.objects.filter(name = file)
    for value in Query.values():
        c1 +=[value[column1]]
        c2 +=[value[column2]]
    c1 = c1[:30]
    c2 = c2[:30]
    print(c1)
    plt.style.use('seaborn')
    plt.title(column1+' and ' + column2 )
    plt.xlabel(column1)
    plt.ylabel(column2)
    plt.scatter(c1, c2 , alpha=0.5)
    path = str(os.getcwd())+"/data/static/media/plot1.png"
    plt.savefig(path)
    path = str(os.getcwd())+"/data/static/media/plot2.png"
    plt.savefig(path)
    return path
 