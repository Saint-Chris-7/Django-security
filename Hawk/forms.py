from django.db import models
from django.forms import ModelForm, fields
from .models import User_data

class user_data_form(ModelForm):
    class Meta:
        models=User_data
        exclude=["qr_code "]
        