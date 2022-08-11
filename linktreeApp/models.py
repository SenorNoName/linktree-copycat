from email.policy import default
import profile
from django.db import models
from django.contrib.auth.models import User
from linkpreview import link_preview

#profile class includes User model, profile picture, and links
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

#OneToMany model, creates a url associated with user's profile
class Link(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f'{self.profile} Links'