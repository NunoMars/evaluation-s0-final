from django.test import TestCase
from django.urls import reverse


class AccountsPagesTest(TestCase):
    def test_create_account_page(self):
        url = reverse("ball8")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "ball8/ball8.html")
        self.assertEqual(response.status_code, 200)
