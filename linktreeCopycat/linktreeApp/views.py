from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Book

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib import messages

#from django.contrib.auth import get_user_model
#User = get_user_model()
#users = User.objects.all()

def index(request):
    return render(request, 'index.html')

def book_by_id(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'book_details.html', {'book':book})
    #return HttpResponse(f"Book: {book.title}, published on {book.pub_date}")

#def user_page(request, user_id):
    #user = User.objects.get(pk=user_id)
    #return render(request, "user_details.html", {'user':user})

def profile(request, username):
    uid = User.objects.filter(username=username).first()
    return render(request, 'profile.html', {'username':username, 'uid':uid})

@login_required
def my_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'my_profile.html', context)