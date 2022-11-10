import contextlib
from django.shortcuts import render
from .logic import clairvoyant
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import MajorArcana
from accounts.models import CustomUser, History, DailySortedCards


def index(request):
    args = {
        "first_title": "Benvenu/e dans mon monde",
        "second_title": "TAROT T",
    }

    return render(request, "home.html", args)


def clairvoyance(request):
    args = {'page_title': 'Tarot'}

    return render(request, "clairvoyance/clairvoyance.html", args)


def card_deck(request):
    cards = MajorArcana.objects.all()
    args = {"cards": cards}
    return render(request, "clairvoyance/card_deck.html", args)


def card_detail(request, card):

    card = MajorArcana.objects.get(id=card)
    args = {"card": card}
    return render(request, "clairvoyance/card_detail.html", args)


def clairvoyante(request):

    if request.method != "POST":
        return
    with contextlib.suppress(ValueError):
        input_value = request.POST.get("messageInput")
        result = clairvoyant(input_value)

        if input_value == "rec":
            return _extracted_from_clairvoyante_9(request, result)
        return JsonResponse(result)

# TODO Rename this here and in `clairvoyante`
def _extracted_from_clairvoyante_9(request, result):
    if not request.user.is_authenticated:
        return JsonResponse(
            {
                "subject": "Error_record",
                "message": "Vos devez vous loguer afin de pouvoir enregistrer"
                + " le tirage, si pas de compte vous devez en créer un en haut sur la barre de Menu!",
            }
        )
    user = request.user
    user = CustomUser.objects.get(email=user.email)

    h_save = History(
        user=user, sorted_card=result[0], chosed_theme=result[1]
    )
    h_save.save()

    return JsonResponse(
        {
            "subject": "succes_rec",
            "message": "Le tirage est à présent enregistré!",
        }
    )



@login_required()
def user_history(request):
    """Fonction for show the user's sorted cards,
     login required."""
    user = request.user
    user = CustomUser.objects.get(email=user.email)

    user_history = History.objects.filter(user=user)
    daily_user_card = DailySortedCards.objects.filter(user=user)

    context = {
        "user": user,
        "user_history": user_history,
        "daily_user_card": daily_user_card,
    }
    return render(request, "clairvoyance/history.html", context)


def contacts(request):
    return render(request, "clairvoyance/contacts.html")
