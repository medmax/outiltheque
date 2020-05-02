from django.urls import path
from .import views
from .views import  LoanDetailView
urlpatterns = [
    path('', views.loans_home, name='loans-home'),
    path('loan/new/<int:tool_id>/', views.loans_requestCreation , name='loan-create'),
     path('loan/<int:pk>/', LoanDetailView.as_view(), name='loan-detail'),
  
] 