from django import forms
from .models import Loan, Tool, User

class LoanRequestForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['request_message']