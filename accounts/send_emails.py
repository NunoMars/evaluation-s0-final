from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
import random
from .models import CustomUser
from clairvoyance.models import MajorArcana



def send_welcome_email(user):
    plaintext = get_template('accounts/email_account_created.txt')
    htmly     = get_template('accounts/email_account_created.html')

    context = { 'username': user.first_name }

    if user.user_language == 'en':
        sentence = 'Wellcome to world of Tarot !!! '

    if user.user_language == 'es':
        sentence = 'Benvenido a El mundo del Tarot !!! '

    if user.user_language == 'pt':
        sentence = 'Benvindo ao meu site de cartonância gratuito!!'
    else:
        sentence = 'Benvenu/a a mon site de voyance gratuit !!! '

    subject, from_email, to = sentence, 'patricia.nunes.tarot@gmail.com', user.email
    text_content = plaintext.render(context)
    html_content = htmly.render(context)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def send_one_card_daily_email():
    users = CustomUser.objects.all()
    htmly = get_template('accounts/daily_card.html')
    cards = MajorArcana.objects.all()

    for user in users:
        print(user.send_email)
        if user.send_email:
            card = random.choice(cards)
            print(user.first_name + " l'ordinateur a choisi  " + card.card_name_fr + " !")

            if user.user_language == 'pt':
                sentence = "A Sua carta Tarot do dia"
                context = {
                    "username" : user.get_full_name(),
                    "card_name" : card.card_name_pt,
                    "card_signification_gen" : card.card_signification_gen_pt,
                    "tag_warning" : "Atenção",
                    "card_singnification_warning" : card.card_signification_warnings_pt,
                    "tag_work" : "Trabalho",
                    "card_signification_work" : card.card_signification_work_pt,
                    "tag_love" : "Amor",
                    "card_signification_love" : card.card_signification_love_pt,
                    "card_image" : card.card_image
                }
            if user.user_language == 'en':
                sentence = "Your daily card!"
                context = {
                    "username" : user.get_full_name(),
                    "card_name" : card.card_name_en,
                    "card_signification_gen" : card.card_signification_gen_en,
                    "tag_warning" : "Atenção",
                    "card_singnification_warning" : card.card_signification_warnings_en,
                    "tag_work" : "Trabalho",
                    "card_signification_work" : card.card_signification_work_en,
                    "tag_love" : "Amor",
                    "card_signification_love" : card.card_signification_love_en,
                    "card_image" : card.card_image
                }
            if user.user_language == 'es':
                sentence = "A tua carta do dia"
                context = {
                    "username" : user.get_full_name(),
                    "card_name" : card.card_name_es,
                    "card_signification_gen" : card.card_signification_gen_es,
                    "tag_warning" : "Atenção",
                    "card_singnification_warning" : card.card_signification_warnings_es,
                    "tag_work" : "Trabalho",
                    "card_signification_work" : card.card_signification_work_es,
                    "tag_love" : "Amor",
                    "card_signification_love" : card.card_signification_love_es,
                    "card_image" : card.card_image
                }
                
            else:
                sentence = "Ta prevision Tarot Du jour"
                context = {
                    "username" : user.get_full_name(),
                    "card_name" : card.card_name_fr,
                    "card_signification_gen" : card.card_signification_gen_fr,
                    "tag_warning" : "Atenção",
                    "card_singnification_warning" : card.card_signification_warnings_fr,
                    "tag_work" : "Trabalho",
                    "card_signification_work" : card.card_signification_work_fr,
                    "tag_love" : "Amor",
                    "card_signification_love" : card.card_signification_love_fr,
                    "card_image" : card.card_image
                }

            html_content = htmly.render(context)
            msg = EmailMultiAlternatives(
                subject=sentence,
                from_email='patricia.nunes.tarot@gmail.com',
                to=[user.email]             
                )
            msg.attach_alternative(html_content, "text/html")
            msg.send()
        else:
            pass
