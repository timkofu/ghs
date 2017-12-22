
import sys

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from github import Github

from gitstars.models import Project
from gitstars.operations import Ops



class Command(BaseCommand):
    help = 'My initial GitHub stars'

    def handle(self, *args, **options):

        try:
            ops = Ops(
                Github(settings.GH_USERNAME, settings.GH_PASSWORD).get_user(settings.GH_USERNAME).get_starred(), 
                Project.objects.all()
            )
            ops.add_stars()
        except CommandError as e:
            sys.stderr.write(str(e))
