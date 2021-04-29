# Generated by Django 3.2 on 2021-04-28 03:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 4, 27, 22, 53, 11, 576049)),
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='end_time',
            field=models.DateTimeField(default=(16, 30, 0)),
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='start_time',
            field=models.DateTimeField(default=(8, 30, 0)),
        ),
    ]
