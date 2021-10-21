from random import shuffle as suf, choice, randint as rand
from .models import MajorArcana,LeftDeck,RightDeck

    
def response_card(name, index_result_card, chosed_theme):
    """
    Draw the Tarot response, the last card.
    """
    card = MajorArcana.objects.get(pk=index_result_card)
    themes = {
        "love" : card.card_signification_love,
        "work" : card.card_signification_work,
        "gen" : card.card_signification_gen,
    }

    return {
        "user_name": name,
        "card_image": card.card_image.url,
        "card_name": card.card_name,
        "chosed_theme_signification": themes[chosed_theme],
        "warnings" : card.card_signification_warnings,
    }


def polarity_calcul(list_of_polarity):
    """
    Construct the message of polarity of deck cards
    """
    items_on_list = len(list_of_polarity)

    def percentage(items_on_list, count_list):
        return count_list * 100 / items_on_list

    how_positif = list_of_polarity.count("Positif")
    how_negatif = list_of_polarity.count("Negatif")
    percentage_positif = round(percentage(items_on_list, how_positif), 2)
    percentage_negatif = round(percentage(items_on_list, how_negatif), 2)

    print("Nombre d'items_on_list " + str(items_on_list))
    print(how_positif)
    print(how_negatif)
    print(percentage_positif)
    print(percentage_negatif)
    
    if how_negatif != 0 and how_negatif < how_positif:
        return "Résultat plutôt positif avec "+ str(percentage_positif) + "% des cartes!!"

    elif how_positif != 0 and how_positif < how_negatif:
        return "Résultat plutôt négatif avec "+ str(percentage_negatif) + "% des cartes!!"    

    return "Il ya un equilibre dans votre tirage!"

 
def average(chosed_card_deck):
    """
    calcul the cards average.             
    """
    print("liste des cartes " + str(len(chosed_card_deck)))
    ids_list = [card.id for card in chosed_card_deck]

    return sum(ids_list) / len(chosed_card_deck)


# construire tableau
def splitBy(li, n=1):
    """
    Generate the split of the cards list.
    """
    return [li[i : i + n] for i in range(1, len(li), n)]


def create_cards_message(card, chosed_theme):
    """
    Draw a bouton card with the name.
    """

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
        + card.card_name.capitalize()
        + "</p>"
        + "<p>"
        + "Mise en Garde!"
        + "</p>"
        + card.card_signification_warnings
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
    print("liste des polarités " + str(len(list_of_polarity)) + "et liste de cartes" + str(len(list_of_cards)))
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
        list_of_polarity.append(card.card_polarity)

    print("nombre de crates " + str(len(chosed_card_deck)))
    print("Nombre de polarités " + str(len(list_of_polarity)))
    message_card = create_cards_message(card, chosed_theme)
    list_of_cards.append(message_card)
    final = create_final_response(
        list_of_cards, name, list_of_polarity, chosed_card_deck
    )
    index_final_card = final[1]
    response = response_card(name, index_final_card, chosed_theme)

    final[0]["response_card"] = response
    return final[0], index_final_card
