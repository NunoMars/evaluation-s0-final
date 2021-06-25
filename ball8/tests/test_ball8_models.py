from django.test import TestCase
from ball8.models import Sentences


class Ball8ModelsTest(TestCase):

    def test_sentence_create(self):
        sentence = Sentences.objects.create(
            sentence = "Test sentence"
        )
        self.assertEqual(sentence, "Test sentence")
      