# Generated by Django 4.2.3 on 2023-07-21 11:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_contact_email_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message_text',
            field=models.TextField(default='Enter Your Massage Please...', max_length=5000),
        ),
        migrations.AlterField(
            model_name='contact',
            name='send_date_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 21, 11, 56, 56, 497406)),
        ),
    ]
