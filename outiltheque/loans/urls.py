from django.urls import path
from . import views
from .views import  LoanDetailView
urlpatterns = [
    path('', views.lend_home, name='lend-home'),
    
    path('loan/new/<int:tool_id>/', views.loans_requestCreation , name='loan-create'),
    path('loan/<int:pk>/', LoanDetailView.as_view(), name='loan-detail'),
    path('loan/<int:pk>/accept/', views.loan_accept, name='loan-accept'),
    path('loan/<int:pk>/complete/', views.loan_complete, name='loan-complete'),
    path('loan/score/<int:user_id>/<int:loan_id>/', views.loan_score, name='loan-score'),

    path('borrow', views.borrow_home, name='borrow-home'),
    path('borrow/<int:pk>/', views.borrow_detail, name='borrow-detail'),
    path('borrow/<int:pk>/retrieve', views.borrow_retrieve, name='borrow-retrieve'),
    path('borrow/<int:pk>/returned', views.borrow_returned, name='borrow-returned'),
    path('borrow/score/<int:user_id>/<int:loan_id>/', views.borrow_score, name='borrow-score')

  
] 