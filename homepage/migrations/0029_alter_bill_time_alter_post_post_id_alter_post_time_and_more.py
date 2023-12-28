# Generated by Django 4.2.7 on 2023-12-23 12:19

import datetime
from django.db import migrations, models
import homepage.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0028_post_post_id_alter_bill_time_alter_post_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 23, 19, 19, 42, 177322)),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_id',
            field=models.CharField(default=homepage.models.generate_unique_post_id, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 23, 19, 19, 42, 177322)),
        ),
        migrations.AlterField(
            model_name='product',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 23, 19, 19, 42, 176315)),
        ),
    ]
