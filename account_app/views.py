from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from account_app.forms import RegistrationForm


# Create your views here.


def register_page(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            return redirect("home_app:main")

    else:
        form = RegistrationForm()
        context = {
            "form": form,
        }
        return render(request, "account_app/register_page.html", context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request=request, user=user)
            return redirect("home_app:main")
    else:
        form = RegistrationForm()
        context = {
            "form": form,
        }
        return render(request, "account_app/register_page.html", context)


def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("accounts_app:register")
