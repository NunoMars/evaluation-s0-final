from django.db import models
from django.utils.safestring import mark_safe



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
    card_image = models.ImageField(upload_to = 'MajorArcanaCards')
    card_polarity = models.CharField(
        max_length=10, choices=CHOICES, default="Positif")

    def __str__(self):
        return self.card_name

    def image_tag(self):

        return mark_safe('<img src="%s" width="150" height="150" />' % (self.card_image))

    image_tag.short_description = 'Image'