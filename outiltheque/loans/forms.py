from django import forms
from .models import Loan, Tool, User
from datetime import datetime
from django.db import models

class DateInput (forms.DateInput):
    input_type = 'date'

class LoanRequestForm(forms.ModelForm):
    class Meta:
        model = Loan
        
        fields = ['request_message', 'date_begin', 'date_end']

    date_begin = forms.DateField(widget=DateInput)
    date_end = forms.DateField(widget=DateInput)


    def clean(self):

        cleaned_data = super().clean()
        begin_date = cleaned_data.get("date_begin")
        end_date = cleaned_data.get("date_end")
     
        if end_date < begin_date:
            raise forms.ValidationError (
                "la date de fin du pret ne peut pas etre inférieur à la date de début"
            )
