from django.urls import path, re_path

from django.views.decorators.csrf import csrf_exempt
from .views import clairvoyance, clairvoyante, user_history, card_deck, card_detail


urlpatterns = [
    path("", clairvoyance, name="clairvoyance"),
    path("clairvoyante", csrf_exempt(clairvoyante), name="clairvoyante"),
    path("history", user_history, name="history"),
    path("card_deck", card_deck, name="card_deck"),
    re_path(r"^card_detail/(?P<card>[0-9]+)/$", card_detail, name="card_detail"),
]
