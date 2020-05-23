from django.db import models
from django.contrib.auth.models import User
from toolbox.models import Tool
from discussion.models import Message
from django.utils import timezone
from django.contrib import messages
# Create your models here.

class Loan (models.Model):
    NEW = 'New'
    ACCEPTED = 'Accepted'
    REJECTED = 'Rejected'
    INPROGRESS = 'InProgress'
    TOOLRETURNED = 'ToolReturned'
    COMPLETED = 'Completed'

    request_message = models.TextField()
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    date_published = models.DateTimeField(default=timezone.now)
    date_begin = models.DateField(default=timezone.now)
    date_end = models.DateField(default=timezone.now)
    messages = models.ManyToManyField(Message)
    STATUS = [
    (NEW, 'demandé'),
    (ACCEPTED, 'accepté'),
    (REJECTED, 'refusé'),
    (INPROGRESS, 'prêt en cours'),
    (TOOLRETURNED, 'outil rendu'),
    (COMPLETED, 'terminé'),
    ]
    status = models.CharField(max_length=100, choices=STATUS, default=NEW)

    def accept(self):
        self.status = self.ACCEPTED
        self.save()

    def retrieve(self):
        self.status = self.INPROGRESS
        self.save()
    
    def return_back(self):
        self.status = self.TOOLRETURNED
        self.save()
    
    def complete(self):
        self.status = self.COMPLETED
        self.save()

class UserLoanScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateTimeField(default=timezone.now)
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    comment = models.TextField()
    class Score (models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
    
    score = models.IntegerField(choices=Score.choices)


