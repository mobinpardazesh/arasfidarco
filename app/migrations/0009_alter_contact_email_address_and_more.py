# Generated by Django 4.2.3 on 2023-07-21 11:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_contact_company_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email_address',
            field=models.EmailField(default='YourIde@YourEmailDomain.com --> timas1254@gmail.com', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='send_date_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 21, 11, 52, 12, 371955)),
        ),
    ]
