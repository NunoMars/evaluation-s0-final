from django.test import TestCase
from clairvoyance.models import MajorArcana
from clairvoyance.logic import clairvoyant


class ClairvoyantTest(TestCase):
    def setUp(self):
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

    def test_clairvoyant_usermane_response(self):
        response = clairvoyant("nuno")
        self.assertTrue(response, {"subject": "menu", "user_name": "nuno"})

    def test_clairvoyance_one_response(self):
        clairvoyant("nuno")
        response = clairvoyant("one")
        self.assertTrue(response, {"subject": "one_card"})

    def test_clairvoyance_love_response_cut(self):
        clairvoyant("nuno")
        response = clairvoyant("love")
        self.assertTrue(response, {"subject": "cut"})

    def test_clairvoyance_love_response_left(self):
        clairvoyant("nuno")
        clairvoyant("love")
        response = clairvoyant("left")
        self.assertTrue(response, {"subject": "final_response"})
