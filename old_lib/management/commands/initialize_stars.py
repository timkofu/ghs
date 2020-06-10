
import sys

from django.core.management.base import BaseCommand, CommandError
from django.db.models.base import ObjectDoesNotExist

from gitstars.models import Project
from gitstars.tasks import mega_update
from gitstars.ops import get_ghh



class Command(BaseCommand):
    help = 'My initial GitHub stars'

    def handle(self, *args, **options):

        try:
            mega_update.delay(
                stars=get_ghh().get_starred(),
                savedstars=Project.objects.all(),
                expected_exceptions=ObjectDoesNotExist,
                first_run=True
            )
        except CommandError as e:
            sys.stderr.write(str(e))
