from types import NoneType
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .forms import UserUpdateForm, ProfileUpdateForm

#homepage
def index(request):
    return render(request, 'index.html')

#allows anyone to view another user's profile without being logged in by visiting /profile/their_username
def profile(request, username):
    uid = User.objects.filter(username=username).first()
    #if the user doesn't exist, a HttpResponse is returned notifying the user of this
    if type(uid) is NoneType:
        return HttpResponse("Error: This user does not exist.", content_type='text/plain')
    return render(request, 'profile.html', {'username':username, 'uid':uid})

#allows the user to view their own profile if they're logged in
def my_profile(request):
    #checks if there is a user logged in, if not they are directed to the login page
    if not request.user.is_authenticated:
        return redirect('login')

    #displays Update Profile Info form where users can update their profile info
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'my_profile.html', context)