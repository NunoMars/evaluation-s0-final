from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and password.
    """

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "second_name", "send_email")


######## Email change form ##########


class EmailChangeForm(forms.Form):
    """
    A form that lets a user change set their email while checking for a change in the 
    e-mail.
    """

    error_messages = {
        "email_mismatch": "Les champs des deux adresses e-mail ne correspondent pas.",
        "not_changed": "L'adresse e-mail renseigné est déjà utilisé.",
    }

    new_email1 = forms.EmailField(label="New email address", widget=forms.EmailInput,)

    new_email2 = forms.EmailField(
        label="New email address confirmation", widget=forms.EmailInput,
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(EmailChangeForm, self).__init__(*args, **kwargs)

    def clean_new_email1(self):
        old_email = self.user.email
        new_email1 = self.cleaned_data.get("new_email1")
        if new_email1 and old_email == new_email1:
            raise forms.ValidationError(
                self.error_messages["not_changed"], code="not_changed",
            )
        return new_email1

    def clean_new_email2(self):
        new_email1 = self.cleaned_data.get("new_email1")
        new_email2 = self.cleaned_data.get("new_email2")
        if new_email1 and new_email2 and new_email1 != new_email2:

            raise forms.ValidationError(
                self.error_messages["email_mismatch"], code="email_mismatch",
            )
        return new_email2

    def save(self, commit=True):
        email = self.cleaned_data["new_email1"]
        self.user.email = email
        if commit:
            self.user.save()
        return self.user
