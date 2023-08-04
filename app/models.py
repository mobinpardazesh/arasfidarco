# Create your models here.

from django.db import models
from django.utils import timezone


# Create your models here.

class Customer(models.Model):
    class Role_Choice(models.TextChoices):
        importer = 'importer'
        distributor = 'distributor'
        trader = 'trader'
        specialist = 'specialist'
        Other = 'Other'

    first_name = models.CharField(max_length=100, default="Name")
    last_name = models.CharField(max_length=100, default="Familly")
    mobile_number = models.CharField(max_length=100, default="(+xx)-xxx-xxx-xxxx --> +317846401457")
    company_name = models.CharField(max_length=100, default="Your Company")
    country_name = models.CharField(max_length=100, default="Your Country")
    email_address = models.EmailField(max_length=100, default="Id@Domain.com --> rosa124@gmail.com")
    message_text = models.TextField(max_length=5000, default="Enter Your Massage Please...")
    role_choice = models.CharField(max_length=100, choices=Role_Choice.choices, default=Role_Choice.Other)
    send_date_time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f'{self.first_name.upper()} {self.last_name.upper()} / {self.mobile_number} / {self.email_address} / {self.company_name} / {self.country_name} / {self.role_choice} / {self.send_date_time}'

