from django.test import TestCase
from django.urls import reverse
from clairvoyance.models import MajorArcana


class ClairvoyancePagesTest(TestCase):
    def setUp(self):
        card = MajorArcana.objects.create(
            card_name="carte1",
            card_signification_gen="Signification_gen",
            card_signification_warnings="Signification_warnings",
            card_signification_love="Signification_love",
            card_signification_work="Signification_work",
            card_image="1.jpg",
        )


    def test_index_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_clairvoyance_page(self):
        response = self.client.get(reverse('clairvoyance'))
        self.assertEqual(response.status_code, 200)

    def test_card_deck_page(self):
        response = self.client.get(reverse('card_deck'))
        self.assertEqual(response.status_code, 200)
    
    def test_card_detail_page(self):
        card = MajorArcana.objects.get(card_name="carte1")
        print(card.id)
        response = self.client.get(reverse('card_detail', args=card.id))
        self.assertEqual(response.status_code, 200)

    def test_user_history_page(self):
        response = self.client.get(reverse('history'))
        self.assertEqual(response.status_code, 302)

    def test_history_page(self):
        url = reverse('history')
        response = self.client.get(url)
        self.assertTemplateNotUsed(response, 'accounts/history.html')
        self.failUnlessEqual(response.status_code, 200)

    def test_contacts_page(self):
        response = self.client.get(reverse('contacts'))
        self.assertEqual(response.status_code, 200)