from django.core.management.base import BaseCommand

from panel.models import EmailAccount


class Command(BaseCommand):
    help = "Add E-Mail Account"

    def add_arguments(self, parser):
        parser.add_argument("user", type=str)
        parser.add_argument("password", type=str)

    def handle(self, *args, **options):
        EmailAccount.objects.create(
            user=options["user"],
            password=options["password"],
        )
