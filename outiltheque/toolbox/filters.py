import django_filters
from .models import *

class ToolFilter(django_filters.FilterSet):
    class Meta:
        model = Tool
        fields = {
            'title' : ['icontains'],
            'state_of_use' : ['exact'],
        }