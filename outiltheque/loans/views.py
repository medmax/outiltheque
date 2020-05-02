from django.shortcuts import render, redirect
from .models import Loan, Tool
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (ListView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.decorators import login_required
from .forms import LoanRequestForm
# Create your views here.

@login_required
def loans_home(request):
    loans = Loan.objects.filter(borrower = request.user)
    context = {'loans' : loans}
    return render(request, 'loans/loans_home.html', context)

@login_required
def loans_requestCreation(request, tool_id):
    tool = Tool.objects.get(id = tool_id)
    borrower = request.user
    if (request.method == "POST"):
        r_form = LoanRequestForm(request.POST)
        if r_form.is_valid() :
          loanRequest = r_form.save(commit=False)
          loanRequest.tool = tool
          loanRequest.borrower = borrower
          loanRequest.save()
          messages.success(request, f'Votre demande de pret à été envoyée')
          return redirect('/loans/')
    else:
        r_form = LoanRequestForm()
    
    context = {'tool' : tool, 'r_form' : r_form}
   
  
   
    return render(request, 'loans/loan_form.html', context)
# class LoanCreateView(LoginRequiredMixin, CreateView):
#     model = Loan
#     fields = ['request_message']
#     tool = Tool.objects.get(id = tool_id)
#     def form_valid(self, form):
#         form.instance.borrower = self.request.user
#         return super().form_valid(form)

class LoanDetailView(DetailView):
    model = Loan

