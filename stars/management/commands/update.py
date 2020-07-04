
import sys

from django.core.management.base import BaseCommand, CommandError
from django.db.models.base import ObjectDoesNotExist

from stars.models import Project
from stars.mega_update import MegaUpdate


class Command(BaseCommand):
    help = 'My initial GitHub stars'

    def handle(self, *args, **options):

        try:
            mu = MegaUpdate(
                saved_stars=Project.objects.all(),
                expected_exceptions=ObjectDoesNotExist
            )
            mu.add_stars()
            mu.update_metadata()
            mu.fallen()
        except CommandError as e:
            sys.stderr.write(str(e))
