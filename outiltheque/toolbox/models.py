from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from PIL import Image

# Create your models here.
class Tool(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_published = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='tool_pics')
    STATE_OF_USE = [
    ('New', 'Comme neuf'),
    ('Medium', 'Moyen'),
    ('Old', 'Usé'),
    ]
    state_of_use = models.CharField(max_length=100, choices=STATE_OF_USE, default='Medium')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)  

    def get_absolute_url(self):
        return reverse('tool-detail', kwargs={'pk': self.pk})

