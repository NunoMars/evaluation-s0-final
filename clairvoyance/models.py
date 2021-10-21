from django.db import models
from django.utils.safestring import mark_safe


class MajorArcana(models.Model):
    """ Class to define the mayor cards deck."""

    CHOICES = (("Positif", "Positif"), ("Negatif", "Negatif"), ("Neutral", "neutral"))

    card_name = models.CharField(max_length=50)
    card_signification_gen = models.TextField()
    card_signification_warnings = models.TextField()
    card_signification_love = models.TextField()
    card_signification_work = models.TextField()
    card_image = models.ImageField(upload_to="MajorArcanaCards")
    card_polarity = models.CharField(max_length=10, choices=CHOICES, default="Positif")

    def __str__(self):
        return self.card_name

    def image_tag(self):

        return mark_safe(
            '<img src="%s" width="75" height="75" />' % (self.card_image)
        )

    image_tag.short_description = "Image"




class LeftDeck(models.Model):
    """ Class to define the left deck."""

    card_id = models.ForeignKey(MajorArcana, on_delete=models.CASCADE)

    def __str__(self):  
        return self.card_id.card_name

class RightDeck(models.Model):
    """ Class to define the right deck."""
    
    card_id = models.ForeignKey(MajorArcana, on_delete=models.CASCADE)

    def __str__(self):  
        return self.card_id.card_name