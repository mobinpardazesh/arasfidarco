# Generated by Django 4.2.3 on 2023-07-21 11:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_contctus_company_name_contctus_country_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contctus',
            name='send_date_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 21, 11, 34, 3, 255876)),
        ),
    ]
