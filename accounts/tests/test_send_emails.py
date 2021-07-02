from django.test import TestCase
from accounts.models import CustomUser, DailySortedCards, History
from clairvoyance.models import MajorArcana
from accounts.send_emails import send_welcome_email, send_one_card_daily_email


class SendEmailsTest(TestCase):
    def setUp(self):
        self.user11 = CustomUser.objects.create(
            email="email11@email.com",
            first_name="first_name11",
            second_name="second_name11",
            password="1234567811",
        )
        i = 1
        for i in range(1, 38):
            card = MajorArcana.objects.create(
                card_name="carte1" + str(i),
                card_signification_gen="Signification_gen" + str(i),
                card_signification_warnings="Signification_warnings" + str(i),
                card_signification_love="Signification_love" + str(i),
                card_signification_work="Signification_work" + str(i),
                card_image=str(i) + ".jpg",
            )

    def test_send_welcome_email(self):
        self.user_to_test = CustomUser.objects.get(email="email11@email.com")
        self.assertTrue(send_welcome_email(self.user_to_test) == "Email envoyé")

    def test_send_one_card_daily_email(self):
        send_one_card_daily_email()
        self.assertTrue(send_one_card_daily_email() == "Tous les mails sont envoyés")
    