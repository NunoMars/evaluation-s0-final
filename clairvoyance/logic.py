from django.shortcuts import redirect
from .card_prints import clairvoyante_sort_cards
from .models import LeftDeck, MajorArcana, RightDeck
from .prepare_decks_cards import prepare_decks


def _extracted_from_clairvoyant_64(arg0):
    deck = arg0.objects.all()
    final_tarot_response = clairvoyante_sort_cards(
        user_name, deck, chosed_theme
    )
    return {
        "subject": "final_response",
        "message": final_tarot_response[0],
    }


def clairvoyant(input_value, lang):
    """
    Construct the bot response.
    """
    global user_name
    global chosed_theme

    list_of_words = [
        "one",
        "cut",
        "Quit",
        "love",
        "work",
        "gen",
        "left",
        "right",
        "Yes",
        "No",
    ]

    rand_card = MajorArcana.objects.order_by("?")[0]

    if input_value not in list_of_words or input_value == "Yes":
        user_name = input_value
        return {"subject": "menu", "user_name": user_name}

    elif input_value == "one":
        return _get_response_one_card(rand_card, lang)

    elif input_value in ["love", "work", "gen", "one"]:
        chosed_theme = input_value

        return {"subject": "cut", "user_name": user_name}

    elif input_value == "cut":

        decks = prepare_decks()
        len_left_deck = decks[0].count()
        len_right_deck = decks[1].count()
        return {
            "subject": "choose_deck",
            "len_left_deck": str(len_left_deck),
            "len_right_deck": str(len_right_deck),
        }

    elif input_value == "No":
        return redirect("home")

    elif input_value == "left":
        return _extracted_from_clairvoyant_64(LeftDeck)

    elif input_value == "right":
        return _extracted_from_clairvoyant_64(RightDeck)


def _get_response_one_card(rand_card, lang):
    if lang == "en":
        card_name = rand_card.card_name_en
        card_signification_warnings = rand_card.card_signification_warnings_en
        card_signification_love = rand_card.card_signification_love_en
        card_signification_work = rand_card.card_signification_work_en
        card_signification_gen = rand_card.card_signification_gen_en

    elif lang == "fr":
        card_name = rand_card.card_name_fr
        card_signification_warnings = rand_card.card_signification_warnings_fr
        card_signification_love = rand_card.card_signification_love_fr
        card_signification_work = rand_card.card_signification_work_fr
        card_signification_gen = rand_card.card_signification_gen_fr

    elif lang == "pt":
        card_name = rand_card.card_name_pt
        card_signification_warnings = rand_card.card_signification_warnings_pt
        card_signification_love = rand_card.card_signification_love_pt
        card_signification_work = rand_card.card_signification_work_pt
        card_signification_gen = rand_card.card_signification_gen_pt

    elif lang == "es":
        card_name = rand_card.card_name_es
        card_signification_warnings = rand_card.card_signification_warnings_es
        card_signification_love = rand_card.card_signification_love_es
        card_signification_work = rand_card.card_signification_work_es
        card_signification_gen = rand_card.card_signification_gen_es

    return {
        "subject": "one_card",
        "user_name": user_name,
        "card_image": rand_card.card_image.url,
        "card_name": card_name,
        "card_signification_warnings": card_signification_warnings,
        "card_signification_love": card_signification_love,
        "card_signification_work": card_signification_work,
        "card_signification_gen": card_signification_gen,
    }
