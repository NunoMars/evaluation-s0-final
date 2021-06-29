from django.test import TestCase
from accounts.models import CustomUser, CustomUserManager


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
        self.assertEqual(user.first_name, 'first_name')
        self.assertEqual(user.second_name, 'second_name')
        self.assertEqual(user.password, '12345678')

    def test_custom_user_manager(self):

        self.user2 = CustomUser.objects.create_user(
            email="email2@email.com",
            first_name="first_name2",
            second_name="second_name2",
            password="123456782"
        )
        self.user_to_test = CustomUser.objects.get(email="email2@email.com")
        self.assertEqual(self.user2, self.user_to_test)

class SuperUserCreationTest(TestCase):
    def test_super_user_creation(self):
        self.user10 = CustomUser.objects.create_superuser(
                email="email10@email.com",
                password="123456782"
            )
        
        self.user_to_test2 = CustomUser.objects.get(email="email10@email.com")
        self.assertTrue(self.user_to_test2.is_superuser)
