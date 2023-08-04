from django.forms import ModelForm
from app.models import Customer

class Customerform(ModelForm):
        class Meta:
            model=Customer
            # fields='__all__'
            fields = ["first_name", "last_name", "mobile_number", "company_name", "country_name", "email_address",
                      "message_text", "role_choice", ]
            labels = {"first_name": "Name", "last_name": "Familly Name", "mobile_number": "Mobile Number",
                      "company_name": "Your Company", "Country Name": "Your Country", "email_address": "Email",
                      "message_text": "Your Message", "role_choice": "Your Role", }
