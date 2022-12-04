from django.db import models


class ResponsesBookEn(models.Model):
    """Class to define the response sentences."""

    sentence_title = models.TextField()
    sentence = models.TextField()

    def __str__(self):
        return f"{self.sentence_title}"


class ResponsesBookFr(models.Model):
    """Class to define the response sentences."""

    sentence_title = models.TextField()
    sentence = models.TextField()

    def __str__(self):
        return f"{self.sentence_title}"


class ResponsesBookPt(models.Model):
    """Class to define the response sentences."""

    sentence_title = models.TextField()
    sentence = models.TextField()

    def __str__(self):
        return f"{self.sentence_title}"


class ResponsesBookEs(models.Model):
    """Class to define the response sentences."""

    sentence_title = models.TextField()
    sentence = models.TextField()

    def __str__(self):
        return f"{self.sentence_title}"
