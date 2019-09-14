from django import forms
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ExtendedUser
from django.core.exceptions import ValidationError




class UpdateExcelForm(forms.Form):
 excel_file = forms.FileField(label='Excel File')    