from django.contrib import admin

# Register your models here.
from .models import Loan, UserLoanScore
admin.site.register(Loan)
admin.site.register(UserLoanScore)