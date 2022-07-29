from django.shortcuts import render, redirect
from .forms import RegisterForm

#registers user with info inputted into form if valid
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/login")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form":form})