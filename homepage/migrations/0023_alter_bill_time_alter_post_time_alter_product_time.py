# Generated by Django 4.2.7 on 2023-12-14 13:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0022_merge_20231212_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 14, 20, 8, 37, 244526)),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 14, 20, 8, 37, 244526)),
        ),
        migrations.AlterField(
            model_name='product',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 14, 20, 8, 37, 243526)),
        ),
    ]
