from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from .backend import CustomUserAuth as CuA
from .forms import CustomUserCreationForm, EmailChangeForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from .send_emails import send_welcome_email


def create_account_view(request):
    """
    Ceates user account
    """
    language = request.LANGUAGE_CODE

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            second_name = form.cleaned_data["second_name"]
            password = form.cleaned_data["password2"]
            send_email = form.cleaned_data['send_email']

            
            user = authenticate(request, username=email, password=password)

            if user == None:
                user = CustomUser.objects.create_user(
                    password=password,
                    first_name=first_name,
                    second_name=second_name,
                    email=email,
                    send_email=send_email,
                )
                user.save()

                login(request, user)
                send_welcome_email(user)
            else:
                login(request, user)

            return render(request, "clairvoyance/history.html")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CustomUserCreationForm()

    return render(request, "accounts/create_account.html", {"form": form})


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect("home")

####### email change #######

@login_required() 
def email_change(request):
    user = request.user
    user = CustomUser.objects.get(email=user.email)
    form = EmailChangeForm(user)
    if request.method=='POST':
        form = EmailChangeForm(user, request.POST)
        if form.is_valid():
            form.save()
            return redirect("history")            
    else:
        form =EmailChangeForm(user)
    
    return render(request, "accounts/email_change.html", {'form':form})