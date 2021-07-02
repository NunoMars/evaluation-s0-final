from siteVoyanceconfig.settings import BASE_DIR
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from django.urls import reverse
from accounts.models import CustomUser


class TestIntegrations(StaticLiveServerTestCase):
    """Functional tests using the Chrome web browser in headless mode."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-extensions")

        cls.driver = webdriver.Chrome(
            executable_path=str(BASE_DIR / "chromedriver"), options=chrome_options,
        )
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.driver.quit()

    def test_create_account(self):
        """
        Tests the account creation page an verify that the account icon change.
        """

        url = reverse("create_account")
        self.driver.get(self.live_server_url + url)

        username_input = self.driver.find_element_by_name("email")
        username_input.send_keys("user20@email.com")

        first_name_input = self.driver.find_element_by_name("first_name")
        first_name_input.send_keys("user")

        second_name_input = self.driver.find_element_by_name("second_name")
        second_name_input.send_keys("vight")

        send_email_input = self.driver.find_element_by_name("send_email")
        send_email_input.send_keys("True")

        password1_input = self.driver.find_element_by_name("password1")
        password1_input.send_keys("a.345679")

        password2_input = self.driver.find_element_by_name("password2")
        password2_input.send_keys("a.345679")

        self.driver.find_element_by_id("create_account").click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "auth_icon"))
        )

        self.assertTrue(element.is_displayed())

    def test_user_can_connect_and_disconnect(self):
        """
        Tests the login and logout pages.
        """

        user = CustomUser.objects.create_user(
            email="souris@purbeurre.com",
            first_name="souris",
            second_name="petite",
            password="a.1234S1",
        )

        url = reverse("login")
        self.driver.get(self.live_server_url + url)

        username = self.driver.find_element_by_id("id_username")
        username.send_keys("souris@purbeurre.com")

        password = self.driver.find_element_by_id("id_password")
        password.send_keys("a.1234S1")

        self.driver.find_element_by_id("login").click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "auth_icon"))
        )

        self.assertTrue(element.is_displayed())

        url = reverse("logout")
        self.driver.get(self.live_server_url + url)

        element = self.driver.find_element_by_id("account_icon")
        self.assertTrue(element.is_displayed())
