# Generated by Django 4.2.7 on 2023-12-04 03:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_alter_bill_time_alter_manager_num_stars_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 4, 10, 8, 18, 654523)),
        ),
        migrations.AlterField(
            model_name='bill',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 4, 10, 8, 18, 654523)),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 4, 10, 8, 18, 654523)),
        ),
    ]
