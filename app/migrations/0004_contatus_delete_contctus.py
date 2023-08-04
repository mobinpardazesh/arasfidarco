# Generated by Django 4.2.3 on 2023-07-21 11:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_contctus_send_date_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(default='+xx-xxx-xxx-xxxx', max_length=100)),
                ('company_name', models.CharField(default='My Company', max_length=100)),
                ('country_name', models.CharField(default='My Country', max_length=100)),
                ('email_address', models.EmailField(default='myname@mydomain.com', max_length=100)),
                ('message_text', models.TextField(default='', max_length=5000)),
                ('role_choice', models.CharField(choices=[('importer', 'Importer'), ('distributor', 'Distributor'), ('trader', 'Trader'), ('specialist', 'Specialist'), ('Other', 'Other')], default='Other', max_length=100)),
                ('send_date_time', models.DateTimeField(default=datetime.datetime(2023, 7, 21, 11, 39, 40, 371542))),
            ],
        ),
        migrations.DeleteModel(
            name='Contctus',
        ),
    ]
