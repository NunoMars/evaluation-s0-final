from django.shortcuts import render, redirect
from django.conf import settings
from .logic import clairvoyant
from django.http import Http404, JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import MajorArcana
from accounts.models import CustomUser, History, DailySortedCards
from django.contrib.auth.models import User
import datetime


def index(request):
    args= {
        "first_title" : "Benvenu/e dans mon monde",
        "second_title" : "TAROT T",
        }

    return render(request, 'home.html', args)


def clairvoyance(request):
    args = {}
    page_title = "Tarot"
    args["page_title"]= page_title
    
    return render(request, 'clairvoyance/clairvoyance.html', args)

def card_deck(request):
    args = {}
    cards = MajorArcana.objects.all()
    args["cards"] = cards
    return render(request, 'clairvoyance/card_deck.html', args)

def card_detail(request, card):

    args = {}
    card = MajorArcana.objects.get(id=card)
    args["card"] = card
    return render(request, 'clairvoyance/card_detail.html', args)

def clairvoyante(request):

    if request.method == 'POST':
        try:
            input_value = request.POST.get('messageInput')
            result = clairvoyant(input_value)

            if input_value == "rec":
                if request.user.is_authenticated:
                    user = request.user
                    user = CustomUser.objects.get(email=user.email)

                    try:
                        save = History(
                        user = user,
                        sorted_card = result[0],
                        chosed_theme = result[1]
                        )
                        save.save()
                        return JsonResponse({
                            "subject" : "succes_rec",
                            'message': "Le tirage est à présent enregistré!"
                        })

                    except:
                        return JsonResponse(
                            {
                                "subject": "Error_record",
                                'message': "UPS!!! Impossible d'enregistrer le tirage, réessayez plus tard svp!"
                            }
                        )
                        
                else:
                    return JsonResponse(
                        {
                            "subject" : "rec_response",
                            'messages': '<a href="{% url '+ 'history' +' %}"' + ">Afin de sauvevarder vous devez être logué! Connectez-vous ICI! et revenez pour un autre tirage gratuit!</a>"
                        }
                    )
            
            else:
                return JsonResponse(result)
            
        except ValueError:
            pass
    else:
        pass 

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
        "daily_user_card": daily_user_card
    }
    return render(request, "clairvoyance/history.html", context)

def contacts(request):
    return render(request, 'clairvoyance/contacts.html')

