from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User
from loans.models import UserLoanScore
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__ (self):
        return f'{self.user.username} Profile '

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)        

    def get_score(self):
            score = UserLoanScore.objects.filter(user__username = self.user.username).aggregate(Avg('score')).get('score__avg')
            if (score):
                return round(score, 1)