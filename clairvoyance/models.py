from django.db import models
from django.utils.safestring import mark_safe


class MajorArcana(models.Model):
    """Class to define the mayor cards deck."""

    CHOICES = (
        ("Positif", "Positif"),
        ("Negatif", "Negatif"),
        ("Neutral", "neutral"),
    )

    card_name_fr = models.CharField(max_length=50)
    card_name_pt = models.CharField(default="pt", max_length=50)
    card_name_en = models.CharField(default="en", max_length=50)
    card_name_es = models.CharField(default="es", max_length=50)

    card_signification_gen_fr = models.TextField(default="fr")
    card_signification_gen_pt = models.TextField(default="pt")
    card_signification_gen_en = models.TextField(default="en")
    card_signification_gen_es = models.TextField(default="es")

    card_signification_warnings_fr = models.TextField(default="fr")
    card_signification_warnings_pt = models.TextField(default="pt")
    card_signification_warnings_en = models.TextField(default="en")
    card_signification_warnings_es = models.TextField(default="es")

    card_signification_love_fr = models.TextField(default="fr")
    card_signification_love_pt = models.TextField(default="pt")
    card_signification_love_en = models.TextField(default="en")
    card_signification_love_es = models.TextField(default="es")

    card_signification_work_fr = models.TextField(default="fr")
    card_signification_work_pt = models.TextField(default="pt")
    card_signification_work_en = models.TextField(default="en")
    card_signification_work_es = models.TextField(default="es")

    card_image = models.ImageField(upload_to="MajorArcanaCards")
    card_polarity = models.CharField(
        max_length=10, choices=CHOICES, default="Positif"
    )

    def __str__(self):
        return self.card_name_fr

    def image_tag(self):

        return mark_safe(
            '<img src="%s" width="75" height="75" />' % (self.card_image)
        )

    image_tag.short_description = "Image"


class LeftDeck(models.Model):
    """Class to define the left deck."""

    card_id = models.ForeignKey(MajorArcana, on_delete=models.CASCADE)

    def __str__(self):
        return self.card_id.card_name_fr


class RightDeck(models.Model):
    """Class to define the right deck."""

    card_id = models.ForeignKey(MajorArcana, on_delete=models.CASCADE)

    def __str__(self):
        return self.card_id.card_name_fr
