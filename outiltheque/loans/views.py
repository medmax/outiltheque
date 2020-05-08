from django.shortcuts import render, redirect
from .models import Loan, Tool
from discussion.models import Message
from users.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (ListView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.decorators import login_required
from .forms import LoanRequestForm
from discussion.forms import MessageForm
# Create your views here.

@login_required
def lend_home(request):
    loans = Loan.objects.filter(tool__owner = request.user)
    context = {'loans' : loans}
    return render(request, 'loans/loans_home.html', context)

@login_required
def borrow_detail(request, pk):
    borrow = Loan.objects.get(id = pk)
    msg_from = MessageForm() 
    if (request.method == "POST"):
            msg_form = MessageForm(request.POST)
            if msg_form.is_valid() :
                # ----Création du msg et ajout au pret a mettre dans le model
                msg = msg_form.save(commit=False)
                sender = borrow.borrower
                receiver = borrow.tool.owner
                msg.sender = sender
                msg.receiver = receiver
                msg.save()
                borrow.messages.add(msg)
                messages.success(request, f'Votre message à été envoyée')
            return redirect('/loans/borrow')
    else:
        r_form = LoanRequestForm()
    
    context = {'borrow' : borrow, 'msg_form': msg_from} 
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
          return redirect('/loans/borrow')
    else:
        r_form = LoanRequestForm()
    
    context = {'tool' : tool, 'r_form' : r_form}
   
  
   
    return render(request, 'loans/loan_form.html', context)

@login_required
def loan_accept(request, pk):
    loan = Loan.objects.get(pk = pk)
    loan.accept()
    messages.success(request, f'Le pret à été accepté, un message a été envoyé au locataire pour le prevenir')
    return redirect('/loans/')

@login_required
def loan_complete(request, pk):
    loan = Loan.objects.get(pk = pk)
    loan.complete()
    messages.success(request, f'Le pret est finalisé merci à toi')
    return redirect('/loans/')

@login_required
def borrow_retrieve(request,pk):
    borrow = Loan.objects.get(pk = pk)
    borrow.retrieve()
    messages.success(request, f'tu as confirmé que tu as recupéré l\'outil')
    return redirect('/loans/borrow')

@login_required
def borrow_returned(request,pk):
    borrow = Loan.objects.get(pk = pk)
    borrow.return_back()
    messages.success(request, f'tu as confirmé que tu as rendu l\'outil à son proprietaire, le proprietaire doit confirmer pour terminer la location')
    return redirect('/loans/borrow')

class LoanDetailView(DetailView):
    model = Loan

