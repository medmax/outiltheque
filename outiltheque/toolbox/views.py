from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from .models import Tool
from django.contrib.auth.models import User
from django.views.generic import (ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .filters import ToolFilter
# Create your views here.


def home(request):

    tools = Tool.objects.all()
    context = {
        'tools' : tools
    }
    return render(request, 'toolbox/toolbox_home.html', context)


def tools_filter(request):
    tools = Tool.objects.all()
    tools_count = tools.count()
    tools_filter = ToolFilter(request.GET, queryset = tools)
    tools = tools_filter.qs

    context = {
        'tools' : tools,
        'tools_count': tools_count,
        'tools_filter' :  tools_filter
    }
    return render(request, 'toolbox/toolbox_filter.html', context)



class ToolListView(ListView):
    model = Tool
    template_name = 'toolbox/toolbox_home.html'
    context_object_name = 'tools'

    
class ToolDetailView(DetailView):
    model = Tool

class ToolCreateView(LoginRequiredMixin, CreateView):
    model = Tool
    fields = ['title', 'description', 'state_of_use']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ToolUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Tool
    fields = ['title', 'description', 'state_of_use']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        tool = self.get_object()
        if self.request.user == tool.owner:
            return True
        return False

class ToolDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Tool
    success_url = '/'
    def test_func(self):
        tool = self.get_object()       
        if self.request.user == tool.owner:
            return True
        return False


class UserToolListView(ListView):
    model = Tool
    template_name = 'toolbox/user_tools.html'
    context_object_name = 'tools'

    

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Tool.objects.filter(owner=user)

