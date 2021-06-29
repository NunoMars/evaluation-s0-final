from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
import random
from .models import CustomUser, DailySortedCards
from clairvoyance.models import MajorArcana



def send_welcome_email(user):
    subject = 'Merci de votre création de compte, Monde Du Tarot'
    message = 'Bonjour ' + user.first_name + " ! Vous allez pouvoir recevoir votre tirage de Tarot quotidien par email! MERCI"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email,]
    send_mail( subject, message, email_from, recipient_list )
    return "Email envoyé"

def send_one_card_daily_email():
    users = CustomUser.objects.all()
    cards = MajorArcana.objects.all()
    host_email = settings.EMAIL_HOST_USER

    for user in users:

        if user.send_email == True:
            card = random.choice(cards)
            list_of_daily_cards = DailySortedCards.objects.filter(user=user)
            if len(list_of_daily_cards) == 31:
                DailySortedCards.objects.filter(user=user).delete()
            h_save = DailySortedCards(
                user = user,
                daily_sorted_cards = card,
                )
            h_save.save()

            print(user.first_name + " l'ordinateur a choisi  " + card.card_name + " !")
            # import file with html content
            html_version = 'accounts/daily_card.html'
            card_url ="https://site-voyance.herokuapp.com"+card.card_image.url
            c = {
                "username" : user.get_full_name(),
                "card_name" : card.card_name,
                "card_signification_gen" : card.card_signification_gen,
                "tag_warning" : "Atention",
                "card_singnification_warnings" : card.card_signification_warnings,
                "tag_work" : "Travail",
                "card_signification_work" : card.card_signification_work,
                "tag_love" : "Amour",
                "card_signification_love" : card.card_signification_love,
                "card_image" : card_url
                }
            html_message = render_to_string(html_version, c)

            subject = "Ta prevision Tarot Du jour"

            message = EmailMessage(subject, html_message, host_email, [user.email])
            message.content_subtype = 'html'
            message.send()
    return "Tous les mails sont envoyés"
