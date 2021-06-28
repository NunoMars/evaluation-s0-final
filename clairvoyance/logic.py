from django.db.models.fields import CharField
from django.utils.translation import gettext as _
from random import shuffle as choice, randint as rand
from .card_prints import clairvoyante_sort_cards
from accounts.models import CustomUser, History
from .models import MajorArcana
from django.contrib.auth.decorators import login_required


@login_required
def recordTirage(card, theme, user):
    card = MajorArcana.objects.filter(card_name=card.card_name)
    theme = "Tirage Rapide"
    message = "Sauvegarde réussie"
    return [card, theme, message]

def clairvoyant(input_value):
    """
        Construct the bot response.
    """

    card_deck = MajorArcana.objects.all()

    list_of_words = ["one", 'cut', 'Quit', 'love', 'work', 'gen', 'left', 'right', 'rec', 'rec_no']

    global chosed_theme
    global deck_choice
    global user_name
    global result

    rand_card = MajorArcana.objects.order_by('?')[0]     

    cards_in_deck = card_deck.count()
    cut_point = rand(1, cards_in_deck)
    left_deck = card_deck[1:cut_point]
    right_deck = card_deck[cut_point:cards_in_deck]

    if input_value not in list_of_words:
        user_name = input_value
        return {
                        "subject" : "menu",
                        "user_name" : user_name
                    }
      

    elif input_value == "one":
        chosed_theme = "one"
        return {
            "subject" : "one_card",
            "user_name" : user_name,
            "card_image" : rand_card.card_image.url,
            'card_name': rand_card.card_name,
            "card_signification_warnings": rand_card.card_signification_warnings,
            "card_signification_love": rand_card.card_signification_love,
            "card_signification_work": rand_card.card_signification_work,
            "card_signification_gen": rand_card.card_signification_gen,
        }

    if input_value == "love":
        chosed_theme = "love"
        return {
        "subject" : "cut"
    }

    if input_value == "work":
        chosed_theme = "work"
        return {
        "subject" : "cut"
    }         

    if input_value == "gen":
        chosed_theme = "gen"            
        return {
            "subject" : "cut"
        }
    

    if input_value == "cut":

        return {
            "subject" : "choose_deck",
            "len_left_deck" : str(len(left_deck)),
            "len_right_deck" : str(len(right_deck))
        }

    # chose the deck
    if input_value == "left":
        deck_choice = left_deck

    if input_value == "right":
        deck_choice = right_deck          

    if input_value == "rec_no":
        return {
            "subject": "rec_no",
            "user_name" : user_name
            }

        result = clairvoyante_sort_cards(user_name, deck_choice, chosed_theme)
                #recording session
    if input_value == "rec":
        if chosed_theme == "one":
            card = rand_card
            theme = "Tirage Rapide"
        
        else:
            card = MajorArcana.objects.filter(id=result[1])
            theme =chosed_theme           
        return [card, theme]  
    else:
        result = clairvoyante_sort_cards(user_name, deck_choice, chosed_theme)
        return {
            "subject" : "final_response",
            "message" : result[0]
        }