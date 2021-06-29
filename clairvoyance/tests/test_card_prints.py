from django.test import TestCase
from accounts.models import CustomUser
from clairvoyance.models import MajorArcana
from clairvoyance.card_prints import response_card


class CardsPrintTest(TestCase):
    def setUp(self):
        i = 1
        for i in range(1, 38):
            card = MajorArcana.objects.create(
                card_name="carte1" + str(i),
                card_signification_gen="Signification_gen" + str(i),
                card_signification_warnings="Signification_warnings" + str(i),
                card_signification_love="Signification_love" + str(i),
                card_signification_work="Signification_work" + str(i),
                card_image=str(i)+ ".jpg",
            )

        self.name = 'Nuno'

    def test_response_card(self):
        self.card_to_test = MajorArcana.objects.get(card_name="carte13")
        self.assertTrue(response_card(self.name, self.card_to_test.id, "love") == {
            "user_name" : "Nuno",
            "card_image" : "/media/3.jpg",
            "card_name": "carte13",
            "chosed_theme_signification" : "Signification_love3",
        })