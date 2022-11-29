# Generated by Django 4.1.3 on 2022-11-27 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_datacsv_delete_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datacsv',
            name='average_monthly_hours',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='datacsv',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='datacsv',
            name='last_evaluation',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='datacsv',
            name='num_project',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='datacsv',
            name='satisfaction_level',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='datacsv',
            name='time_spend_comapny',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='datacsv',
            name='work_accident',
            field=models.BooleanField(blank=True, default=0),
        ),
    ]
