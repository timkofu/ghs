
from django.conf import settings
from django.db import IntegrityError
#from django.db.transaction import atomic
from django.core.management.base import BaseCommand, CommandError

from github import Github

from gitstars.models import Language, Project

from gitstars.operations import Ops



class Command(BaseCommand):
    help = 'My initial GitHub stars'

    #@atomic
    def handle(self, *args, **options):

        my_github_handle = Github(settings.GH_USERNAME, settings.GH_PASSWORD)
        my_stars = my_github_handle.get_user(settings.GH_USERNAME).get_starred()
        ops = Ops(my_stars, None)

        # Add new stars
        ops.add_stars({'language':Language, 'project':Project}, expected_exceptions=IntegrityError)
