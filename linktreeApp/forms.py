from django import forms
from django.contrib.auth.models import User
from .models import Link, Profile

#updates username and email of User and Profile databases
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

#updates profile picture of Profile database
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

#updates link database
class LinkUpdateForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['url']