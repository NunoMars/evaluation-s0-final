from django.urls import path
from . import views


urlpatterns = [
    path("", views.ball8, name="ball8"),
]
