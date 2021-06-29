from random import shuffle as suf, choice, randint as rand
from .models import MajorArcana


def response_card(name, index_result_card, chosed_theme):
    """
    Draw the Tarot response, the last card.
    """
    card = MajorArcana.objects.get(pk=index_result_card)

    card_name = card.card_name

    if chosed_theme == "love":

        chosed_theme_signification = card.card_signification_love

    if chosed_theme == "work":

        chosed_theme_signification = card.card_signification_work

    if chosed_theme == "gen":

        chosed_theme_signification = card.card_signification_gen

    return {
        "user_name": name,
        "card_image": card.card_image.url,
        "card_name": card.card_name,
        "chosed_theme_signification": chosed_theme_signification,
    }


def polarity_calcul(list_of_polarity):
    """
    Construct the message of polarity of deck cards
    """
    items_on_list = len(list_of_polarity)

    def percentage(items_on_list, count_list):
        percentage = count_list * 100 / items_on_list
        return percentage

    how_positif = list_of_polarity.count("Positif")
    if how_positif != 0:
        percentage_positif = round(percentage(items_on_list, how_positif), 2)
    else:
        percentage_positif = 0

    how_negatif = list_of_polarity.count("Negatif")
    if how_negatif != 0:
        percentage_negatif = round(percentage(items_on_list, how_negatif), 2)
    else:
        percentage_negatif = 0

    how_neutral = list_of_polarity.count("Neutral")

    if how_neutral != 0:
        percentage_neutral = round(percentage(items_on_list, how_neutral), 2)
    else:
        percentage_neutral = 0

    if percentage_positif == 0 or percentage_negatif == 0 or percentage_neutral == 0:
        if list_of_polarity[0] == "Positif":
            msg = [
                "Résultat plutôt positif avec "
                + str(percentage_positif)
                + "% des cartes!!"
            ]
        if list_of_polarity[0] == "Negatif":
            msg = [
                " Tirage négatif avec "
                + str(percentage_negatif)
                + "%, mais le tarot vous montre le chemin ...!"
            ]
        if list_of_polarity[0] == "Neutral":
            msg = ["Il ya un equilibre dans votre tirage!"]
        return msg[0]


def average(chosed_card_deck):
    """
    calcul the cards average.             
    """
    ids_list = []
    for card in chosed_card_deck:
        ids_list.append(card.id)

    return sum(ids_list) / chosed_card_deck.count()


# construire tableau
def splitBy(li, n=1):
    """
    Generate the split of the cards list.
    """
    return [li[i : i + n] for i in range(0, len(li), n)]


def create_cards_message(card, chosed_theme):
    """
    Draw a bouton card with the name.
    """
    card_name = card.card_name
    card_signification_warnings = card.card_signification_warnings

    msg = [
        "<div class='col'>"
        + "<div class='cta-inner text-center rounded'>"
        + "<a href='#'><img class='card' src='/static/img/cards/Back.jpg'"
        + "onmouseover="
        + '"this.src='
        + "'"
        + card.card_image.url
        + "'"
        + '"'
        + "onmouseout="
        + "this.src='/static/img/cards/Back.jpg'"
        + " alt=''/>"
        + "<span><p>"
        + card_name.capitalize()
        + "</p>"
        + "<p>"
        + "Mise en Garde!"
        + "</p>"
        + card_signification_warnings
        + "<p>"
        + "ce que signifie la carte!"
        + "</p>"
        + chosed_theme
        + "</span></a></div></div>"
    ]
    return msg[0]


def create_final_response(list_of_cards, name, list_of_polarity, chosed_card_deck):
    """ 
    Construct the cards board and generate the response heads tittle.
    """

    column = 6
    index_result_card = round(average(chosed_card_deck))
    card_board = splitBy(list_of_cards, column)

    final_card_deck = []
    for i in card_board:
        l = "".join(i)
        final_card_deck.append(
            "<div class='row' height= '100%' text-align='center'>" + l + "</div>"
        )

    f = "".join(final_card_deck)

    polarity = polarity_calcul(list_of_polarity)

    final_tittle = {
        "final_response_tittle": "<div class='col'><div class='cta-inner text-center rounded'>"
        + "<h4>"
        + name.capitalize()
        + " vois-ci votre réponse!"
        + "</h4>"
        + "<h4>"
        + polarity
        + "</h4>"
        + "<h6>"
        + "Afin de voir les mises en garde, survolez la carte avec la souris..."
        + "</h6>"
        + f
        + "</div>"
    }

    return final_tittle, index_result_card


def clairvoyante_sort_cards(name, chosed_card_deck, chosed_theme):
    """
        Construct the last response of sorted cards.
    """
    list_of_cards = []
    list_of_polarity = []

    for card in chosed_card_deck:
        card_polarity = card.card_polarity
        list_of_polarity.append(card_polarity)

        message_card = create_cards_message(card, chosed_theme)
        list_of_cards.append(message_card)
        final = create_final_response(
            list_of_cards, name, list_of_polarity, chosed_card_deck
        )
        index_final_card = final[1]
        response = response_card(name, index_final_card, chosed_theme)

        final[0]["response_card"] = response
    return final[0], index_final_card
