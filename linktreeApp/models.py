from email.policy import default
from django.db import models
from django.contrib.auth.models import User

#profile class includes User model, profile picture, and links
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    links = models.CharField(max_length=500, default='https://www.google.com/')

    def __str__(self):
        return f'{self.user.username} Profile'