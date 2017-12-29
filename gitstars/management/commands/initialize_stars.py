
import sys

from django.core.management.base import BaseCommand, CommandError

from gitstars.models import Project
from gitstars.operations import Ops, github_handle



class Command(BaseCommand):
    help = 'My initial GitHub stars'

    def handle(self, *args, **options):

        try:
            ops = Ops(
                github_handle.get_starred(), 
                Project.objects.all()
            )
            ops.add_stars()
        except CommandError as e:
            sys.stderr.write(str(e))
