from django.utils.translation import gettext as _
from random import shuffle as suf, choice, randint as rand
from .card_prints import one_card, clairvoyante_sort_cards
from accounts.models import History
from .models import MajorArcana
from django.contrib.auth.decorators import login_required

inputs = []


def clairvoyant(input_value):
    """
        Construct the bot reponse.
    """
    card_deck = [i+1 for i in range(38)]
    global inputs
    if input_value not in inputs:
        inputs.append(input_value)


    user_name = inputs[0]

    user_choices = {"messages": "<div class='cta-inner text-center rounded'>" +
    "<div class='row'>" +
    "<div class='col'>" +
    "<p><h6>" + "Merci beaucoup " + user_name.capitalize() + " !</h6></p>" +
    "<p><h5>" + " Je mélange les lâmes du tarot..." + "</h5></p></div></div>" +
    "<div class='row'>" +
    "<div class='col'>" +
    "<p><h5>" + "Choisissiez le domaine de la question!" + "</h5></p>" +
    "<p><h6>" + "Cliquez sur le paquet de cartes svp!" + "</h6></p></div></div>" +
    "<div class='row'>" +
    "<div class='col'>" +
    "<p><h6>" + "AMOUR" + "<h6></p>" +
    "<p><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageLove();'/></p></div>" +
    "<div class='col'>" +
    "<p><h6>" + "TRAVAIL" + "</h6></p>" +
    "<p><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageWork();'/></p></div>" +
    "<div class='col'>" +
    "<p><h6>" + " TIRAGE GENERAL" + "</h6></p>" +
    "<p><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageGen();'/></p></div>" +
    "<div class='col'>" +
    "<p><h6>" + "TIRAGE RAPIDE" + "</h6></p>" +
    "<p><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageOneCard();'/></p></div>" +
    "</div></div>"
    }

   
    record = {"message" :  "<div class='cta-inner text-center rounded'>" +
    "<div class='row'>" +
    "<div class='col'>" +
    "<p><h3>" + "Voulez-vous enregistrer le tirage?" + "</h3></p></div></div>" +
    "<div class='row'>" +
    "<div class='col'>" +
    "<p><h6>" + "SAUVEGARDER" + "</h6></p>" +
    "<p><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageRecYes();'/></p></div>" +
    "<div class='col'>" + "<p><h6>" + "NON" + "</h6></p>" +
    "<p><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageRecNo();'/></p></div>" +
    "</div></div>"
    }

    message_cut = {"messages": "<div class='cta-inner text-center rounded'>" +
    "<div class='row'>" +
    "<div class='col'>" + 
    "<p><h4>" + "Merci beaucoup " + user_name.capitalize() + " !</h4></p>" +
    " <p>" + "Encore une chose svp!" + "</p>" +
    " <p>" + "Cliquez afin de couper le jeu de cartes!" + 
    "</p></div></div>" +
    "<div class='row'>" +
    "<div class='col'>" + 
    "<input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageCut();'/></div>" +
    "</div></div></div>"
    }


    while True:        

        if input_value == "Quit":
            inputs = []

        if len(inputs) == 1:
            return user_choices

        if input_value == "one":
            card_deck = [i+1 for i in range(38)]
            suf(card_deck)

            global rand_card
            rand_card = choice(card_deck)
            
            value = one_card(user_name, rand_card)
            return {'messages' : value + record['message']}        

        if input_value == "love":
            inputs[1] = "love"
            return message_cut

        if input_value == "work":
            inputs[1] = "work"
            return message_cut

        if input_value == "gen":
            inputs[1] = "gen"
            return message_cut
        

        if input_value == "cut":
            cut_point = rand(1, 37)
            inputs[2] = cut_point
            left_deck = card_deck[0:cut_point]
            right_deck = card_deck[cut_point:37]

            return {"messages": "<div class='col'><div class='cta-inner text-center rounded'>" +
                    "<p class='mb-0'><h4>" +"Merci !" + "</h4></p>" +
                    "<p class='mb-0'>" + "On a donc deux paquets de cartes!" + "</p>" +
                    "<p class='mb-0'>" + "Cliques sur celui de votre choix svp!" + "</p></div></div>" +
                    "<div class='row'>" +
                    "<div class='col''><div class='cta-inner text-center rounded'>" +
                    "<h1>Ce paquet a " + str(len(left_deck)) + " cartes!" +
                    "<div class='mb-0'><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageLeft();'/></div></div></div>" +
                    "<div class='col''><div class='cta-inner text-center rounded'>" +
                    "<h1>Celui ci a " + str(len(right_deck)) + " cartes!" +
                    "<div class='mb-0'><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageRight();'/></div></div></div>" +
                    "</div>"
                    }

        # chose the deck
        if input_value == "left":
            inputs[3] = card_deck[0:inputs[2]]

        if input_value == "right":
            inputs[3] = card_deck[inputs[2]:37]


        if input_value == "rec":
            if inputs[1] == "one":
                card = MajorArcana.objects.filter(id=rand_card)
                theme = "Tirage Rapide"
                
            else:
                index_card = round(sum(inputs[3])/len(inputs[3]))
                card = MajorArcana.objects.filter(id=index_card)
                theme =inputs[1]

            del inputs[1:]                
            return [card[0], theme, user_choices]        
            

        if input_value == "rec_no":
            del inputs[1:]
            return user_choices

        result = clairvoyante_sort_cards(user_name, inputs[3], inputs[1])
        return {'messages' : result["messages"] + record['message']}

