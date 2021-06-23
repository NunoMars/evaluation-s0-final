from django.test import TestCase
from accounts.models import CustomUser
from accounts.backend import CustomUserAuth

class UserBackendTest(TestCase):
    def setUp(self):
        user = CustomUser.objects.create(
            email="email@email.com",
            first_name="first_name",
            second_name="second_name",
            password="12345678"
        )


    def test_Custom_user_auth(self):
        user = CustomUser.objects.get(email="email@email.com")
        assert self.assertIsNone(CustomUserAuth.authenticate(user.email, user.password))
