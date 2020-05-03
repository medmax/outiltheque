from django import forms
from .models import Loan, Tool, User

class DateInput (forms.DateInput):
    input_type = 'date'

class LoanRequestForm(forms.ModelForm):
    class Meta:
        model = Loan
        
        fields = ['request_message', 'date_begin', 'date_end']

    date_begin = forms.DateField(widget=DateInput)
    date_end = forms.DateField(widget=DateInput)

