from .models import CsvData

def inserting(uploaded_file):
    """
    fetching the data from the file and uploading it to the data base. 
    """
    i = 0   
    with open(uploaded_file.name, 'r') as data:
        for row in data.readlines():
            v = row.split(',')
            i+=1
            if v[0] == 'satisfaction_level':
                continue
        
            values = CsvData(name=uploaded_file.name.replace('.csv', ""),department=v[-1].replace('\n', ''), 
                            satisfaction_level= float(v[0]), 
                            last_evaluation =float(v[1]), 
                            num_project =float(v[2]),
                            average_monthly_hours =int(v[3]), 
                            time_spend_comapny= int(v[4]), 
                            work_accident=int(v[5]))
            values.save()
            
        return True
    