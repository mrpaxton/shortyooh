# provide the command for django admin custom command

from django.core.management.base import BaseCommand, CommandError
from shortener.models import ShortURL

class Command(BaseCommand):
    help = "Referesh all ShortURL shortcodes."

    def add_arguments(self, parser):
        parser.add_argument('items', type=int)

    def handle(self, *args, **options):
        return ShortURL.objects.refresh_shortcodes(items=options['items'])
