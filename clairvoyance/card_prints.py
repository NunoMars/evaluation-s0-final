from random import shuffle as suf, choice, randint as rand
from django.utils.translation import gettext as _
from datetime import datetime
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


    response = {"messages": "<div class='col cta-inner text-center rounded'>" +
            "<h2>" + name.capitalize() + " c ce-ci est le votre message, ce que le Tarot a vous dire!" + "</h2>" +
            "<a href='#'><img src='/static/img/cards/Back.jpg'" +
            "onmouseover=" + '"this.src=' + "'/" + card.card_image.url + "'" + '"' +
            " alt='' height='15%' width='15%'/>" +
            "<p><h3>" + card_name.capitalize() + "</h3></p>" +
            "<div class='mb-0'><h3>" + "Réponse" + "</h3></div>" +
            "<p class='mb-0'>" + chosed_theme_signification + "</p>" +
            "</div>"
            }
    return response['messages']



def clairvoyante_sort_cards(name, chosed_card_deck, chosed_theme):

    card_deck = list(MajorArcana.objects.all())
    suf(card_deck)
    column = 6

    # construire tableau
    def splitBy(li, n=1):
        return [li[i:i+n] for i in range(0, len(li), n)]

    def create_cards_message(card, chosed_theme):
        '''
        Draw a bouton card with the name.
        '''
        card_name = card.card_name
        card_signification_warnings = card.card_signification_warnings

        msg = ["<div class='col'>" +
               "<div class='cta-inner text-center rounded'>" +
               "<a href='#'><img class='card' src='/static/img/cards/Back.jpg'" +
               "onmouseover=" + '"this.src=' + "'/" + card.card_image.url + "'" + '"' +
               "onmouseout=" + "this.src='/static/img/cards/Back.jpg'" +
               " alt=''/>" +
               "<span><p>" + card_name.capitalize() + "</p>" +
               "<p>" + "Mise en Garde!" + "</p>" + card_signification_warnings +
               "<p>" + "ce que signifie la carte!" + "</p>" + chosed_theme +
               "</span></a>" +
               "</div></div>"]
        return msg

    def create_final_response(list_of_cards, name, list_of_polarity, chosed_card_deck):

        def polarity_calcul(list_of_polarity):

            items_on_list = len(list_of_polarity)

            def percentage(items_on_list, count_list):
                percentage = count_list * 100/items_on_list
                return percentage

            how_positif = list_of_polarity.count('Positif')
            if how_positif != 0:
                percentage_positif = round(
                    percentage(items_on_list, how_positif), 2)
            else:
                percentage_positif = 0

            how_negatif = list_of_polarity.count('Negatif')
            if how_negatif != 0:
                percentage_negatif = round(
                    percentage(items_on_list, how_negatif), 2)
            else:
                percentage_negatif = 0

            how_neutral = list_of_polarity.count('Neutral')
            
            if how_neutral != 0:                
                percentage_neutral = round(
                    percentage(items_on_list, how_neutral), 2)
            else:
                percentage_neutral = 0

            if percentage_positif == 0 or percentage_negatif == 0 or percentage_neutral == 0:
                if list_of_polarity[0] == "Positif":
                    msg = ["Résultat plutôt positif!"]
                if list_of_polarity[0] == "Negatif":
                    msg = ["Résultat plutôt négatif"]
                if list_of_polarity[0] == "Neutral":
                    msg = ["Il ya un equilibre dans votre tirage!"]
                return msg[0]

            if percentage_positif > percentage_negatif or percentage_positif > percentage_neutral:
                msg = [
                    " Tirage positif avec " +
                    str(percentage_positif) + _("% des cartes!")
                ]
                return msg[0]

            if percentage_negatif > percentage_positif or percentage_negatif > percentage_neutral:
                msg = [
                    " Tirage négatif avec " + str(percentage_negatif) +
                    "%, mais le tarot vous montre le chemin ...!"
                ]
                return msg[0]
            if percentage_neutral >= percentage_positif or percentage_neutral >= percentage_negatif:
                msg = [
                    "Tirage equilibré"
                ]
                return msg[0]

        def average(chosed_card_deck):
            return sum(chosed_card_deck)/len(chosed_card_deck)

        index_result_card = round(average(chosed_card_deck))

        important_card = response_card(
            name, index_result_card, chosed_theme)

        card_board = splitBy(list_of_cards, column)

        final_card_deck = []
        for i in card_board:
            l = ''.join(i)
            final_card_deck.append(
                "<div class='row' height= '100%' text-align='center'>" + l + "</div>")

        f = ''.join(final_card_deck)

        polarity = polarity_calcul(list_of_polarity)


        return {"messages": "<div class='col'><div class='cta-inner text-center rounded'>" +
                "<h4>" + name.capitalize() + _(" vois-ci votre réponse!") + "</h4>" +
                "<h4>" + polarity + "</h4>" +
                "<h6>" + "Afin de voir les mises en garde, survolez la carte avec la souris..." + "</h6>" +
                f + "</div>" + important_card
                }

    list_of_cards = []
    list_of_polarity = []  

    for i in chosed_card_deck:
        card = MajorArcana.objects.get(pk=i)
        card_polarity = card.card_polarity
        list_of_polarity.append(card_polarity)
    
        message_card = create_cards_message(card, chosed_theme)
        list_of_cards.append(message_card[0])

    return create_final_response(list_of_cards, name, list_of_polarity, chosed_card_deck)
