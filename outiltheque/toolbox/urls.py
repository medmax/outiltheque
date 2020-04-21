from django.urls import path
from .import views
from .views import ToolListView, ToolDetailView, ToolCreateView, ToolUpdateView, ToolDeleteView, UserToolListView

urlpatterns = [
    path('', ToolListView.as_view(), name='toolbox-home'),
    path('tool/<int:pk>/', ToolDetailView.as_view(), name='tool-detail'),
    path('tool/new/', ToolCreateView.as_view(), name='tool-create'),
    path('tool/<int:pk>/update/', ToolUpdateView.as_view(), name='tool-update'),
    path('tool/<int:pk>/delete/', ToolDeleteView.as_view(), name='tool-delete'),
    path('user/<str:username>', UserToolListView.as_view(), name='user-tools'),
] 