from django.test import TestCase
from django.urls import reverse


class AccountsPagesTest(TestCase):
    def test_create_account_page(self):
        url = reverse("create_account")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "accounts/create_account.html")
        self.assertEqual(response.status_code, 200)

    def test_log_out(self):
        url = reverse("logout")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_email_change_page(self):
        url = reverse("email_change")
        response = self.client.get(url)
        self.assertTemplateNotUsed(response, "accounts/email_change.html")
        self.failUnlessEqual(response.status_code, 302)
