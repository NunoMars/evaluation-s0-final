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
            phone_number = form.cleaned_data['phone_number']
            send_email = form.cleaned_data['send_email']
            send_text_message = form.cleaned_data['send_text_message']
            
            user = authenticate(request, username=email, password=password)

            if user == None:
                user = CustomUser.objects.create_user(
                    password=password,
                    first_name=first_name,
                    second_name=second_name,
                    email=email,
                    phone_number=phone_number,
                    send_email=send_email,
                    send_text_message=send_text_message,
                )
                user.save()

                login(request, user)
                send_welcome_email(user)
            else:
                login(request, user)

            return render(request, "accounts/thanks.html")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CustomUserCreationForm()

    return render(request, "accounts/create_account.html", {"form": form})


def login_view(request):

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(CuA, username=username, password=password)

    if user is not None:
        login(request, user)
        # Redirect to a success page.
        msg = "Bienvenu"
        return render(request, "accounts/my_account.html", {"msg": msg})
    else:
        # Return an 'invalid login' error message.
        msg = "Compte utilisateur non trouvé!"
        vars_to_template = {
            "msg": msg,
            "link": "../create_account",
            "link_msg": "Créez un compte utilisateur!",
        }

        return render(request, "accounts/my_account.html", vars_to_template)

    return render(request, "accounts/my_account.html")


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect("home")

####### email change #######

@login_required() 
def email_change(request):
    user = request.user
    user = CustomUser.objects.get(email=user)
    form = EmailChangeForm(user)
    if request.method=='POST':
        form = EmailChangeForm(user, request.POST)
        if form.is_valid():
            form.save()
            print(user.email)
            return redirect("history")            
    else:
        form =EmailChangeForm(user)
    
    return render(request, "accounts/email_change.html", {'form':form})