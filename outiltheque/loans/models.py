from django.db import models
from django.contrib.auth.models import User
from toolbox.models import Tool
from django.utils import timezone
# Create your models here.

class Loan (models.Model):

    request_message = models.TextField()
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    date_begin = models.DateField(default=timezone.now)
    date_end = models.DateField(default=timezone.now)