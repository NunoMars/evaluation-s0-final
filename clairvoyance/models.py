from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class MajorArcana(models.Model):
    """ Class to define the mayor cards deck."""
    CHOICES = (
        ("Positif", "Positif"),
        ("Negatif", "Negatif"),
        ("Neutral", "neutral")
    )

    card_name = models.CharField(max_length=50)
    card_signification_gen = models.TextField()
    card_signification_warnings = models.TextField()
    card_signification_love = models.TextField()
    card_signification_work = models.TextField()
    card_image = models.CharField(max_length=100)
    card_polarity = models.CharField(
        max_length=10, choices=CHOICES, default="Positif")
