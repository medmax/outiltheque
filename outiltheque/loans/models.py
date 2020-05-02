from django.db import models
from django.contrib.auth.models import User
from toolbox.models import Tool
# Create your models here.

class Loan (models.Model):

    request_message = models.TextField()
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    