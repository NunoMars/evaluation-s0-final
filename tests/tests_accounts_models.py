from django.test import TestCase
from accounts.models import CustomUser


class UserCreationTest(TestCase):
    def setUp(self):
        user = CustomUser.objects.create(
            email="email@email.com",
            first_name="first_name",
            second_name="second_name",
            password="12345678"
        )
        

    def test_user(self):
        user = CustomUser.objects.get(email="email@email.com")
        self.assertEqual(user.email, "email@email.com")


