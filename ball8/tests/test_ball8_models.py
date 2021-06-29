from django.test import TestCase
from ball8.models import Sentences


class Ball8ModelsTest(TestCase):
    def test_sentence_create(self):
        sentence = Sentences.objects.create(sentence="Test sentence")
        s = Sentences.objects.get(sentence="Test sentence")

        self.assertEqual(s.sentence, "Test sentence")
        self.assertEqual(s.sentence_polarity, "Positif")
        self.assertEqual(str(s), "Test sentence, Positif")
