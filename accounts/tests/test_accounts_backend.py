from django.test import TestCase
from accounts.models import CustomUser
from accounts.backend import CustomUserAuth

class UserBackendTest(TestCase):
    def setUp(self):
        self.user5 = CustomUser.objects.create(
            email="email5@email.com",
            first_name="first_name5",
            second_name="second_name5",
            send_email=True
        )
        self.user5.set_password = "123456785"
        self.user5.save()


    def test_Custom_user_auth(self):

        self.user = CustomUser.objects.get(email="email5@email.com")
        self.assertTrue((CustomUserAuth.authenticate("email5@email.com", "123456785"), self.user))
        self.assertIsNone((CustomUserAuth.authenticate("toto@toto.com")))