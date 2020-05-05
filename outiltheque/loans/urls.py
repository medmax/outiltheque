from django.urls import path
from .import views
from .views import  LoanDetailView
urlpatterns = [
    path('', views.lend_home, name='lend-home'),
    path('borrow', views.borrow_home, name='borrow-home'),
    path('loan/new/<int:tool_id>/', views.loans_requestCreation , name='loan-create'),

    path('loan/<int:pk>/', LoanDetailView.as_view(), name='loan-detail'),
    path('loan/<int:pk>/accept/', views.loan_accept, name='loan-accept'),
    path('borrow/<int:pk>/', views.borrow_detail, name='borrow-detail'),
    path('borrow/<int:pk>/retrieve', views.borrow_retrieve, name='borrow-retrieve'),
  
] 