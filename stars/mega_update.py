from github import Github
from django.conf import settings

from stars.models import Project, ProgrammingLanguage


class MegaUpdate:
    __slots__ = (
        'stars',
        'first_run',
        'saved_stars',
        'expected_exceptions',
    )

    def __init__(self, saved_stars, expected_exceptions, first_run=False) -> None:
        self.first_run = first_run
        self.saved_stars = saved_stars
        self.expected_exceptions = expected_exceptions
        self.stars = Github(settings.GITHUB_ACCESS_TOKEN)\
            .get_user(settings.GITHUB_USERNAME) \
            .get_starred()

    def add_stars(self) -> None:
        """ Add new stars """

        addables = [s for s in self.stars if s.name in {  # star object if (valid) star not already saved
            s.name for s in self.stars if all([s.name, s.html_url])  # valid stars (name & url set)
        } - {
            p[0] for p in self.saved_stars.values_list('name')  # already saved stars
        }]  # in valid stars but not in saved stars

        # Now we save the new ones
        for s in addables:
            Project(
                name=s.name,
                full_name=s.full_name or 'N/A',
                description=s.description or 'N/A',
                url=s.html_url,
                initial_stars=s.stargazers_count,
                current_stars=s.stargazers_count,
                language=ProgrammingLanguage.objects.get_or_create(name=s.language or 'N/A')[0]
            ).save()

    def update_metadata(self) -> None:
        """ Update starcount and descriptions """

        for star in self.stars:
            try:
                saved_star = self.saved_stars.get(full_name=star.full_name)
                if saved_star:
                    if saved_star.current_stars != star.stargazers_count:
                        saved_star.current_stars = star.stargazers_count
                    elif star.description and saved_star.description != star.description:
                        saved_star.description = star.description
                    elif star.full_name and saved_star.full_name != star.full_name:
                        saved_star.full_name = star.full_name
                    saved_star.save()
            except self.expected_exceptions:
                continue

    def fallen(self) -> None:
        """ Delete unstared projects (fallen stars) """

        current_stars = {x.full_name for x in self.stars}
        stored_stars = {x.full_name for x in self.saved_stars}
        for fs in stored_stars - current_stars:
            self.saved_stars.get(full_name=fs).delete()
