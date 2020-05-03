from django import forms
from .models import Loan, Tool, User


class DateInput (forms.DateInput):
    input_type = 'date'

class LoanRequestForm(forms.ModelForm):
    class Meta:
        model = Loan
        date_begin = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
        date_end = forms.DateField(widget= forms.TextInput(attrs={'class': 'datepicker'}))
        fields = ['request_message', 'date_begin', 'date_end']
