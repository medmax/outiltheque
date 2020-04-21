from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Tool(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_published = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    STATE_OF_USE = [
    ('New', 'Comme neuf'),
    ('Medium', 'Moyen'),
    ('Old', 'Usé'),
    ]
    state_of_use = models.CharField(max_length=100, choices=STATE_OF_USE, default='Medium')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tool-detail', kwargs={'pk': self.pk})