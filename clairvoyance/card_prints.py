from random import shuffle as suf, choice, randint as rand
from django.utils.translation import gettext as _
from datetime import datetime
from .models import MajorArcana


def one_card(name, rand_card, language):
    """
        Rends one cart response.
    """
    card = MajorArcana.objects.get(pk=rand_card)

    if language == 'pt' or language == 'br':
        card_name = card.card_name_pt
        card_signification_warnings = card.card_signification_warnings_pt
        card_signification_gen = card.card_signification_gen_pt
        card_signification_love = card.card_signification_love_pt
        card_signification_work = card.card_signification_work_pt

    if language == 'en':
        card_name = card.card_name_en
        card_signification_warnings = card.card_signification_warnings_en
        card_signification_gen = card.card_signification_gen_en
        card_signification_love = card.card_signification_love_en
        card_signification_work = card.card_signification_work_en

    if language == 'es':
        card_name = card.card_name_es
        card_signification_warnings = card.card_signification_warnings_es
        card_signification_gen = card.card_signification_gen_es
        card_signification_love = card.card_signification_love_es
        card_signification_work = card.card_signification_work_es
    else:
        card_name = card.card_name_fr
        card_signification_warnings = card.card_signification_warnings_fr
        card_signification_gen = card.card_signification_gen_fr
        card_signification_love = card.card_signification_love_fr
        card_signification_work = card.card_signification_work_fr

    response = {"messages": "<div class='col cta-inner text-center rounded'>" +
            "<h2>" + name.capitalize() + _(" o que o tarot tem para lhe dizer!") + "</h2>" +
            "<a href='#'><img src='/static/img/cards/Back.jpg'" +
            "onmouseover=" + '"this.src=' + "'/" + card.card_image + "'" + '"' +
            " alt='' height='15%' width='15%'/>" +
            "<p><h3>" + card_name.capitalize() + "</h3></p>" +
            "<div class='mb-0'><h3>" + _("Atenção") + "</h3></div>" +
            "<p class='mb-0'>" + card_signification_warnings + "</p>" +
            "<div class='mb-0'><h4>" + _("Significado en geral") + "</h4></div>" +
            "<p class='mb-0'>" + card_signification_gen + "</p>" +
            "<div class='mb-0'><h4>" + _("No amor") + "</h4></div>" +
            "<p class='mb-0'>" + card_signification_love + "</p>" +
            "<div class='mb-0'><h4>" + _("No trabalho") + "</h4></div>" +
            "<p class='mb-0'>" + card_signification_work + "</p>" +
            "</div>"
            }

    return response['messages']


def response_card(name, index_result_card, chosed_theme, language):
    """
    Draw the Tarot response, the last card.
    """
    card = MajorArcana.objects.get(pk=index_result_card)
    if language == 'en':
        card_name = card.card_name_en
    if language == 'pt' or language == 'br':
        card_name = card.card_name_pt
    if language == 'es':
        card_name = card.card_name_es
    else:
        card_name = card.card_name_fr

    if chosed_theme == "love":
        
        if language == 'es':        
            chosed_theme_signification = card.card_signification_love_es

        if language == 'en':        
            chosed_theme_signification = card.card_signification_love_en
            
        if language == 'pt' or language == 'br':
            chosed_theme_signification = card.card_signification_love_pt

        else:
            chosed_theme_signification = card.card_signification_love_fr
            chosed_theme ="Amour"

    if chosed_theme == "work":
        if language == 'es':
            chosed_theme_signification = card.card_signification_work_es

        if language == 'en':
            chosed_theme_signification = card.card_signification_work_en

        if language == 'pt' or language == 'br':
            chosed_theme_signification = card.card_signification_work_pt

        else:
            chosed_theme_signification = card.card_signification_work_fr

    if chosed_theme == "gen":
        if language == 'es':
            chosed_theme_signification = card.card_signification_gen_es

        if language == 'en':
            chosed_theme_signification = card.card_signification_gen_en

        if language == 'pt' or language == 'br':
            chosed_theme_signification = card.card_signification_gen_pt

        else:
            chosed_theme_signification = card.card_signification_gen_fr


    response = {"messages": "<div class='col cta-inner text-center rounded'>" +
            "<h2>" + name.capitalize() + _(" o que o tarot tem para lhe dizer!") + "</h2>" +
            "<a href='#'><img src='/static/img/cards/Back.jpg'" +
            "onmouseover=" + '"this.src=' + "'/" + card.card_image + "'" + '"' +
            " alt='' height='15%' width='15%'/>" +
            "<p><h3>" + card_name.capitalize() + "</h3></p>" +
            "<div class='mb-0'><h3>" + _("Resposta do tarot") + "</h3></div>" +
            "<p class='mb-0'>" + chosed_theme_signification + "</p>" +
            "</div>"
            }
    return response['messages']



def clairvoyante_sort_cards(name, chosed_card_deck, chosed_theme, language ):

    card_deck = list(MajorArcana.objects.all())
    suf(card_deck)
    column = 6

    # construire tableau
    def splitBy(li, n=1):
        return [li[i:i+n] for i in range(0, len(li), n)]

    def create_cards_message(card, chosed_theme, language):
        '''
        Draw a bouton card with the name.
        '''

        if language == 'es':
            card_name = card.card_name_es
            card_signification_warnings = card.card_signification_warnings_es
        if language == 'en':
            card_name = card.card_name_en
            card_signification_warnings = card.card_signification_warnings_en
        if language == 'pt' or language == 'br':
            card_name = card.card_name_pt
            card_signification_warnings = card.card_signification_warnings_pt
        else:
            card_name = card.card_name_fr
            card_signification_warnings = card.card_signification_warnings_fr

        msg = ["<div class='col'>" +
               "<div class='cta-inner text-center rounded'>" +
               "<a href='#'><img class='card' src='/static/img/cards/Back.jpg'" +
               "onmouseover=" + '"this.src=' + "'/" + card.card_image + "'" + '"' +
               "onmouseout=" + "this.src='/static/img/cards/Back.jpg'" +
               " alt=''/>" +
               "<span><p>" + card_name.capitalize() + "</p>" +
               "<p>" + _("Atenção") + "</p>" + card_signification_warnings +
               "<p>" + _("A mensagen da carta!") + "</p>" + chosed_theme +
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
                    msg = [_("O resultado é positivo!")]
                if list_of_polarity[0] == "Negatif":
                    msg = [_("O resultado é negativo!")]
                if list_of_polarity[0] == "Neutral":
                    msg = [_("O resultado e revelado pela carta que segue!")]
                return msg[0]

            if percentage_positif > percentage_negatif or percentage_positif > percentage_neutral:
                msg = [
                    _(" O resultado é positivo com ") +
                    str(percentage_positif) + _("% total de cartas a favor!")
                ]
                return msg[0]

            if percentage_negatif > percentage_positif or percentage_negatif > percentage_neutral:
                msg = [
                    _(" O resultado é negativo com ") + str(percentage_negatif) +
                    _("% total de cartas en desfavor, mâs, tudo tem solução o Tarot vai-lhe indicar o caminho...!")
                ]
                return msg[0]
            if percentage_neutral >= percentage_positif or percentage_neutral >= percentage_negatif:
                msg = [
                    _("O resultado revela o equilibrio com ") + str(percentage_neutral) + _("% das cartas!") +
                    _("! Nem muito nem pouco, mas ha sempre aspectos que podem que ser melhorados!")
                ]
                return msg[0]

        def average(chosed_card_deck):
            return sum(chosed_card_deck)/len(chosed_card_deck)

        index_result_card = round(average(chosed_card_deck))

        important_card = response_card(
            name, index_result_card, chosed_theme, language)

        card_board = splitBy(list_of_cards, column)

        final_card_deck = []
        for i in card_board:
            l = ''.join(i)
            final_card_deck.append(
                "<div class='row' height= '100%' text-align='center'>" + l + "</div>")

        f = ''.join(final_card_deck)

        polarity = polarity_calcul(list_of_polarity)
        print(polarity)

        return {"messages": "<div class='col'><div class='cta-inner text-center rounded'>" +
                "<h4>" + name.capitalize() + _(" aqui esta o resultado das cartas") + "</h4>" +
                "<h4>" + polarity + "</h4>" +
                "<h6>" + _("Para saber os avisos do Tarot passe o rato en cima de cada carta!") + "</h6>" +
                f + "</div>" + important_card
                }

    list_of_cards = []
    list_of_polarity = []  

    for i in chosed_card_deck:
        card = MajorArcana.objects.get(pk=i)
        card_polarity = card.card_polarity
        list_of_polarity.append(card_polarity)
    
        message_card = create_cards_message(card, chosed_theme, language)
        list_of_cards.append(message_card[0])

    return create_final_response(list_of_cards, name, list_of_polarity, chosed_card_deck)
