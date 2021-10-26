from django.test import TestCase
from clairvoyance.models import MajorArcana
from clairvoyance.logic import clairvoyant
from clairvoyance.prepare_decks_cards import prepare_decks


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
            i += 1

        decks = prepare_decks()
        self.right_deck = decks[1]
        self.left_deck = decks[0]

    def test_clairvoyant_usermane_response(self):
        response = clairvoyant("nuno")
        self.assertTrue(response, {"subject": "menu", "user_name": "nuno"})

    def test_clairvoyance_one_response(self):
        self._extracted_from_test_clairvoyance_love_response_left_2(
            "nuno", "one", "one_card"
        )

    def test_clairvoyance_love_response_cut(self):
        self._extracted_from_test_clairvoyance_love_response_left_2(
            "nuno", "love", "cut"
        )

    def test_clairvoyance_love_response_left(self):
        clairvoyant("nuno")
        self._extracted_from_test_clairvoyance_love_response_left_2(
            "love", "left", "final_response"
        )

    # TODO Rename this here and in `test_clairvoyance_one_response`, `test_clairvoyance_love_response_cut` and `test_clairvoyance_love_response_left`
    def _extracted_from_test_clairvoyance_love_response_left_2(self, arg0, arg1, arg2):
        clairvoyant(arg0)
        response = clairvoyant(arg1)
        self.assertTrue(response, {'subject': arg2})
