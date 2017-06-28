
from django.conf import settings
from django.db.transaction import atomic
from django.core.management.base import BaseCommand, CommandError
from gitstars.models import Language, Project



class Command(BaseCommand):
    help = 'My initial GitHub stars'

    @atomic
    def handle(self, *args, **options):

        my_github_handle = Github(settings.GH_USERNAME, settings.GH_PASSWORD)
        my_stars = self.my_github_handle.get_user(settings.GH_USERNAME).get_starred()
        saved_stars = Project.objects.all()

        # Adding new stars
        for star in my_stars:
            if all([star.name, star.full_name, star.language, star.description,
                star.html_url, star.stargazers_count]):
                try:
                    lang = Language.objects.get_or_create(name=star.language)[0]
                    Project.objects.get_or_create( #update_or_create exists as well :)
                    # should be faster than get_or_create
                    #Project( <-- this breaks the atomic transaction????
                        name=star.name,
                        full_name=star.full_name,
                        description=star.description,
                        url=star.html_url,
                        initial_stars=star.stargazers_count,
                        current_stars=star.stargazers_count,
                        language=lang,
                    )
                except IntegrityError:
                    pass
