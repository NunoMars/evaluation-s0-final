from django.test import TestCase, Client
from accounts.forms import CustomUserCreationForm, EmailChangeForm
from accounts.models import CustomUser


class CustomUserCreationFormTest(TestCase):
    def setUp(self):
        self.user4 = CustomUser.objects.create(
            email="email@email.com",
            first_name="first_name",
            second_name="second_name",
            password="12345678",
        )

    def test_custom_user_creation_form_email_field_label(self):
        form = CustomUserCreationForm()
        self.assertTrue(
            form.fields["email"].label == None or form.fields["email"].label == "Email"
        )

    def test_custom_user_creation_form_first_name_field_label(self):
        form = CustomUserCreationForm()
        self.assertTrue(
            form.fields["first_name"].label == None
            or form.fields["first_name"].label == "First name"
        )

    def test_custom_user_creation_form_second_name_field_label(self):
        form = CustomUserCreationForm()
        self.assertTrue(
            form.fields["second_name"].label == None
            or form.fields["second_name"].label == "Second name"
        )

    def test_custom_user_creation_form_password1_field_label(self):
        form = CustomUserCreationForm()
        self.assertTrue(
            form.fields["password1"].label == None
            or form.fields["password1"].label == "Password"
        )

    def test_custom_user_creation_form_password2_field_label(self):
        form = CustomUserCreationForm()
        self.assertTrue(
            form.fields["password2"].label == None
            or form.fields["password2"].label == "Password confirmation"
        )

    def test_custom_user_creation_form(self):
        form_data = {
            "email": "remi@purbeurre.com",
            "first_name": "Remi",
            "second_name": "PetitChef",
            "password1": "Some.hi1",
            "password2": "Some.hi1",
            "send_email": "True",
        }

        self.form = CustomUserCreationForm(data=form_data)

        self.assertTrue(self.form.is_valid())


class EmailChangeFormTest(TestCase):
    def setUp(self):

        self.user5 = CustomUser.objects.create(
            email="email5@email.com",
            first_name="first_name5",
            second_name="second_name5",
        )
        self.user5.set_password = "123456785"
        self.user5.save()

        client = Client()
        client.login(username="email5@email.com", password="123456785")

    def test_new_email_fields(self):
        form = EmailChangeForm(self.user5)
        self.assertTrue(
            form.fields["new_email1"].label == None
            or form.fields["new_email1"].label == "New email address"
        )

        self.assertTrue(
            form.fields["new_email2"].label == None
            or form.fields["new_email2"].label == "New email address confirmation"
        )

    def test_email_change_form(self):
        form_data = {"new_email1": "123@hotmail.fr", "new_email2": "123@hotmail.fr"}
        form = EmailChangeForm(self.user5, data=form_data)
        self.assertTrue(form.is_valid())
        self.assertTrue(self.user5.email, "123@hotmail.fr")

        