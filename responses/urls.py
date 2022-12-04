from django.urls import path
from . import views


urlpatterns = [
    path("", views.responses, name="responses"),
]
