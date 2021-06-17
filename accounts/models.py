from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.timezone import now
from clairvoyance.models import MajorArcana

from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with teh given email and password.

        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password, **extra_fields):
        """
        #Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=254, blank=True)
    second_name = models.CharField(max_length=254, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(blank=False, unique=True)
    phone_number = models.BigIntegerField(default="0000000000", blank=True)
    send_email = models.BooleanField(default=False)
    send_text_message = models.BooleanField(default=False)
    
    USERNAME_FIELD = "email"


    objects = CustomUserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def get_absolute_url(self):
        return "/users/%s/" % (self.email)

    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.second_name)
        return full_name.strip()

    def __str__(self):
        return f"{self.first_name}, {self.second_name}, {self.email}"


class History(models.Model):
    """ Class to define the History table."""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    sorted_cards_date = models.DateTimeField(auto_now_add=True)
    sorted_card = models.ForeignKey(MajorArcana, verbose_name=_("Tiragem"), on_delete=models.CASCADE)
    chosed_theme = models.CharField(default="theme", max_length=10)

    class Meta:
        db_table = "history"



class DailySortedCards(models.Model):
    """
    rec the daily_cards
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    sorted_cards_date = models.DateTimeField(auto_now_add=True)
    daily_sorted_cards = models.ForeignKey(MajorArcana, verbose_name=_("Tiragem"), on_delete=models.CASCADE)

    class Meta:
        db_table = "daily_cards"
    
