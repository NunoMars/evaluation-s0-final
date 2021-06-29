from accounts.models import CustomUser, DailySortedCards
from django.test import TestCase, client
from django.urls import reverse
from clairvoyance.models import MajorArcana
from accounts.models import History, DailySortedCards


class ClairvoyancePagesTest(TestCase):
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
        user = CustomUser.objects.create(
            email="email@email.com",
            first_name="first_name",
            second_name="second_name",
            password="12345678",
        )
        self.client.login(username="email@email.com", password="12345678")
        rand_card = MajorArcana.objects.order_by("?")[0]
        h = History.objects.create(
            user=user, sorted_card=rand_card, chosed_theme="love"
        )

    def test_index_page(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_clairvoyance_page(self):
        response = self.client.get(reverse("clairvoyance"))
        self.assertEqual(response.status_code, 200)

    def test_card_deck_page(self):
        response = self.client.get(reverse("card_deck"))
        self.assertEqual(response.status_code, 200)

    def test_card_detail_page(self):
        card = MajorArcana.objects.get(card_name="carte11")
        response = self.client.get(reverse("card_detail", args=[card.pk]))
        self.assertEqual(response.status_code, 200)

    def test_user_history_page(self):
        response = self.client.get(reverse("history"))
        self.assertEqual(response.status_code, 302)

    def test_contacts_page(self):
        url = reverse("contacts")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_clairvoyante(self):
        url = reverse("contacts")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
