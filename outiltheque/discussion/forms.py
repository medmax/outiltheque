from django import forms
from .models import Message
from datetime import datetime
from django.db import models


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message        
        fields = ['body']
