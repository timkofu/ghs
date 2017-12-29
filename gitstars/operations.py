
from django.conf import settings

from github import Github

from .models import Project, Language



class Ops:

	def __init__(self, mystars, savedstars):
		self.stars = mystars
		self.savedstars = savedstars


	def add_stars(self):
		''' Add new stars '''

		addables = {
			s.name for s in self.stars if all([s.name,s.html_url]) # name and url needed
		} - {
			p[0] for p in self.savedstars.values_list('name')
		} # Set diff, so we only add what we don't already haves

		# Now we cherry pick the new ones, and get rid of the orig addables object
		addables = [s for s in self.stars if s.name in addables]

		# Now we save the new ones
		Project.objects.bulk_create(
			[Project(
                name=s.name,
                full_name=s.full_name or 'N/A',
                description=s.description or 'N/A',
                url=s.html_url,
                initial_stars=s.stargazers_count,
                current_stars=s.stargazers_count,
                language=Language.objects.get_or_create(name=s.language or 'N/A')[0]
            ) for s in addables]
        )


	def update_metadata(self, expected_exceptions):
		''' Update starcount and descriptions '''
		for star in self.stars:
		    try:
		        saved_star = self.savedstars.get(full_name=star.full_name)
		        if saved_star:
		            if saved_star.current_stars != star.stargazers_count:
		                saved_star.current_stars = star.stargazers_count
		            elif star.description and saved_star.description != star.description:
		                saved_star.description = star.description
		            elif star.full_name and saved_star.full_name != star.full_name:
		                saved_star.full_name = star.full_name
		            saved_star.save()
		    except expected_exceptions:
		        continue


	def fallen(self):
		''' Delete unstared projects (fallen stars) '''
		current_stars = {x.full_name for x in self.stars}
		stored_stars = {x.full_name for x in self.savedstars}
		for fs in stored_stars - current_stars:
		    self.savedstars.get(full_name=fs).delete()

github_handle = Github(settings.GH_USERNAME, settings.GH_PASSWORD).get_user(settings.GH_USERNAME)