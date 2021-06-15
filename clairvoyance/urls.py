from django.urls import path
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from .views import clairvoyance, clairvoyante, user_history, card_deck, card_detail



urlpatterns = [
    path('', clairvoyance, name='clairvoyance'),
    url('clairvoyante', csrf_exempt(clairvoyante), name='clairvoyante'),
    url('history', user_history, name='history'),
    url('card_deck', card_deck, name='card_deck'),
    url('card_detail', card_detail, name='card_detail'),
]