from .models import CsvData

def files_and_columns():
    """
    this function gets the files list and column names from the  Database
    """
    context = {}
    with open("data/static/media/files_list.txt", 'r') as filename:
        context['uploaded_files'] = filename.readlines()

    #getting the list objects 
    form = CsvData.objects.all()

    #getting the column list
    for e in form:
        column_names = list(e.__dict__.keys())
        break
    #Removing the columns that are not required.
    if len(column_names) != 0:
        for remove in ['_state', 'date', 'id', 'name']:
            column_names.remove(remove)

    context['columns'] = column_names

    return context