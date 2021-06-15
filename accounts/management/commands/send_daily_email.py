from django.core.management.base import BaseCommand, CommandError

from accounts.send_emails import send_one_card_daily_email


class Command(BaseCommand):
    def handle(self, *args, **options):

        

        help = "Send a daily email to users."

        print("Start work!")

        try:
            send_one_card_daily_email()          

            print("All emails have been sended !")

        except:
            raise CommandError(
                "Ups une erreur est arrivé, envoi emails aborté!!"
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Done!!"
            )
        )