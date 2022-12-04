from django.core.management.base import BaseCommand
from clairvoyance.models import MajorArcana
from googletrans import Translator

translator = Translator()


class Command(BaseCommand):
    help = "Peuplate database with a json file"

    def handle(self, *args, **options):

        data = MajorArcana.objects.all()

        for i in data:
            print(i.card_name_fr)
            text_pt = translator.translate(
                text=i.card_name_fr,
                src="fr",
                dest="es",
            )

            text_2 = translator.translate(
                text=i.card_signification_gen_fr,
                src="fr",
                dest="es",
            )
            text_3 = translator.translate(
                text=i.card_signification_warnings_fr,
                src="fr",
                dest="es",
            )
            text_4 = translator.translate(
                text=i.card_signification_love_fr,
                src="fr",
                dest="es",
            )
            text_5 = translator.translate(
                text=i.card_signification_work_fr,
                src="fr",
                dest="es",
            )

            i.card_name_es = text_pt.text
            i.card_signification_gen_es = text_2.text
            i.card_signification_warnings_es = text_3.text
            i.card_signification_love_es = text_4.text
            i.card_signification_work_es = text_5.text

            i.save()

            print('%s" Cree en base de données!' % i.card_name_fr)

        self.stdout.write(self.style.SUCCESS("Successfully !!!"))
