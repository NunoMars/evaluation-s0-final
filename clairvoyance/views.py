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
    args = {"page_title": "Tarot"}

    return render(request, "clairvoyance/clairvoyance.html", args)


def card_deck(request):
    cards = MajorArcana.objects.all()
    lang = request.LANGUAGE_CODE

    args = {
        "lang": lang,
        "cards": cards,
    }
    return render(request, "clairvoyance/card_deck.html", args)


def card_detail(request, card):
    card = MajorArcana.objects.get(id=card)
    lang = request.LANGUAGE_CODE
    args = {}
    if lang == "fr":
        args["card_name"] = card.card_name_fr
        args["card_signification_gen"] = card.card_signification_gen_fr
        args["card_signification_love"] = card.card_signification_love_fr
        args["card_signification_work"] = card.card_signification_work_fr
        args[
            "card_signification_warnings"
        ] = card.card_signification_warnings_fr
    if lang == "pt":
        args["card_name"] = card.card_name_pt
        args["card_signification_gen"] = card.card_signification_gen_pt
        args["card_signification_love"] = card.card_signification_love_pt
        args["card_signification_work"] = card.card_signification_work_pt
        args[
            "card_signification_warnings"
        ] = card.card_signification_warnings_pt
    if lang == "en":
        args["card_name"] = card.card_name_en
        args["card_signification_gen"] = card.card_signification_gen_en
        args["card_signification_love"] = card.card_signification_love_en
        args["card_signification_work"] = card.card_signification_work_en
        args[
            "card_signification_warnings"
        ] = card.card_signification_warnings_en
    if lang == "es":
        args["card_name"] = card.card_name_es
        args["card_signification_gen"] = card.card_signification_gen_es
        args["card_signification_love"] = card.card_signification_love_es
        args["card_signification_work"] = card.card_signification_work_es
        args[
            "card_signification_warnings"
        ] = card.card_signification_warnings_es
    args["card_image"] = card.card_image
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

    h_save = History(user=user, sorted_card=result[0], chosed_theme=result[1])
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
