from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from accounts.models import CustomUser, History


class AccountsPagesTest(TestCase):

    def test_create_account_page(self):
        url = reverse('create_account')
        response = self.client.get(url)
        self.assertTemplateNotUsed(response, 'accounts/create_account.html')
        self.assertEqual(response.status_code, 200)

    def test_history_page(self):
        url = reverse('history')
        response = self.client.get(url)
        self.assertTemplateNotUsed(response, 'accounts/history.html')
        self.failUnlessEqual(response.status_code, 200)

    def test_history_page(self):
        url = reverse('email_change')
        response = self.client.get(url)
        self.assertTemplateNotUsed(response, 'accounts/email_change.html')
        self.failUnlessEqual(response.status_code, 302)