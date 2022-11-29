# Generated by Django 4.1.3 on 2022-11-27 11:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=255)),
                ('satisfaction_level', models.FloatField(blank=True, default=0, null=True)),
                ('last_evaluation', models.FloatField(blank=True, default=0, null=True)),
                ('num_project', models.IntegerField(blank=True, default=0, null=True)),
                ('time_spend_comapny', models.IntegerField(blank=True, default=0, null=True)),
                ('work_accident', models.BooleanField(blank=True, default=0, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
