from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Message(models.Model):
    sender = models.ForeignKey(User, null=True, related_name='sender', on_delete=models.SET_NULL)
    receiver = models.ForeignKey(User, null=True, related_name='receiver', on_delete=models.SET_NULL)
    body = models.TextField()
    date_published = models.DateTimeField(default=timezone.now)


    def create (sender, receiver, body):
        msg = Message(sender = sender, receiver = receiver, body = body)
        msg.save()
        return msg