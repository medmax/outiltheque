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
def lend_home(request):
    loans = Loan.objects.filter(tool__owner = request.user)
    context = {'loans' : loans}
    return render(request, 'loans/loans_home.html', context)


@login_required
def borrow_detail(request, pk):
    borrow = Loan.objects.get(id = pk)
    context = {'borrow' : borrow} 
    return render(request, 'loans/borrow_detail.html', context)

@login_required
def borrow_home(request):
    loans = Loan.objects.filter(borrower = request.user)
    context = {'loans' : loans}
    return render(request, 'loans/borrow_home.html', context)

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


def loan_accept(request, pk):
    Loan.objects.filter(pk = pk).update(status='Accepted')
    messages.success(request, f'Le pret à été accepté, un message a été envoyé au locataire pour le prevenir')
    return redirect('/loans/')

def borrow_retrieve(request,pk):
    Loan.objects.filter(pk = pk).update(status='ToolRetrieved')
    messages.success(request, f'tu as confirmé que tu as recupéré l\'outil')
    return redirect('/borrow/')


class LoanDetailView(DetailView):
    model = Loan

