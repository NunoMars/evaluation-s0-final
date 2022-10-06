from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from .views import create_account_view, email_change


urlpatterns = [
    path("create_account/", create_account_view, name="create_account"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("email_change/", email_change, name="email_change"),
    path("login/", LoginView.as_view(template_name="accounts/login.html"), name="login"),
]
