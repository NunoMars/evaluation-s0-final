from django.test import TestCase
from accounts.models import CustomUser
from accounts.send_emails import send_welcome_email, send_one_card_daily_email


class SendEmailsTest(TestCase):
    def setUp(self):
        self.user11 = CustomUser.objects.create(
            email="email11@email.com",
            first_name="first_name11",
            second_name="second_name11",
            password="1234567811",
        )

    def test_send_welcome_email(self):
        self.user_to_test = CustomUser.objects.get(email="email11@email.com")
        self.assertTrue(send_welcome_email(self.user_to_test) == "Email envoyé")

    def test_send_one_card_daily_email(self):
        self.assertTrue(send_one_card_daily_email() == "Tous les mails sont envoyés")
