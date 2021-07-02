from django.test import TestCase, Client, LiveServerTestCase
from django.urls import reverse
from accounts.models import CustomUser

class AccountsPagesTest(LiveServerTestCase):
    def setUp(self):
        CustomUser.objects.create(
            email="email21@email.com",
            first_name="first_name21",
            second_name="second_name21",
            password="1234567821",
        )
        self.client = Client()
        
    def test_create_account_page(self):
        url = reverse("create_account")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "accounts/create_account.html")
        self.assertEqual(response.status_code, 200)

    def test_log_out(self):

        # Log in
        self.client.login(username='email21@email.com', password="1234567821")

        # Check response code
        url = reverse('login')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        # Log out
        self.client.logout()

        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


    def test_log_in(self):

        # Check response code
        url = reverse('login')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


    def test_email_change_page(self):
        url = reverse("email_change")
        response = self.client.get(url)
        self.assertTemplateNotUsed(response, "accounts/email_change.html")
        self.failUnlessEqual(response.status_code, 302)
