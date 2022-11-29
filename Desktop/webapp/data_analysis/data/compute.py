from .models import CsvData
from django.db.models import Max, Min, Sum, Avg

def computation(column, operation, file):
    """
    This will compute accept the operation, filename, column 
    are parameters with which we need to perform the query operation.
    """
    if file == None or column == None or operation == None:
        return ''
    file = file.replace('.csv',"").strip()
    column = column.strip()
    operation = operation.strip()

    print(file)
    Query  = CsvData.objects.filter(name=file)
    
    if operation == 'MAX':
        val = Query.aggregate(Max(column))
        val = val[column+'__max']
    elif operation == 'MIN':
        val= Query.aggregate(Min(column))
        val = val[column+'__min']
    
    elif operation == 'SUM':
        val = Query.aggregate(Sum(column))
        val = val[column+'__sum']

    
    return val
    
