# Generated by Django 4.2.7 on 2023-12-30 16:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_alter_bill_time_alter_comment_time_alter_post_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 30, 23, 8, 55, 685674)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 30, 23, 8, 55, 685674)),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 30, 23, 8, 55, 685674)),
        ),
        migrations.AlterField(
            model_name='product',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 30, 23, 8, 55, 685674)),
        ),
    ]
