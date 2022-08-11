from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm

#registers user with info inputted into form if valid
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            #automatically logs in new user
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'],)
            login(response, new_user)

        return redirect("/profile")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form":form})