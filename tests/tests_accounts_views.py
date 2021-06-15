from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from products.models import Products, Categorys
from accounts.models import CustomUser, History


class AccountsPagesTest(TestCase):

    def test_create_account_page(self):

        response = self.client.get(reverse('create_account'))
        self.assertEqual(response.status_code, 200)

    def test_history_page(self):
        response = self.client.get(reverse('history'))
        self.assertEqual(response.status_code, 302)