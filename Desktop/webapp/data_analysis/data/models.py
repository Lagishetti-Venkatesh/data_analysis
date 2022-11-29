from django.db import models
from django.utils import timezone


class CsvData(models.Model):
    
    name = models.CharField(max_length=255)

    department = models.CharField(max_length=255)

    satisfaction_level = models.FloatField(default=0, blank=True, null=True)

    last_evaluation = models.FloatField(default=0, blank=True, null=True)
    
    num_project = models.IntegerField(default=0, blank=True, null=True)
    
    average_monthly_hours = models.IntegerField(default= 0, blank=True, null=True)
    
    time_spend_comapny = models.IntegerField(default=0, blank=True, null=True)
    
    work_accident = models.BooleanField(default=0, blank=True, null=True)
    
    date = models.DateTimeField(default =timezone.now)
    


    def __str__(self) :
        return self.name