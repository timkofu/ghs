
import pickle
from time import sleep

from django.conf import settings
from django.core.cache import cache

from github import Github

from .models import Project, Language



class Ops:

	def __init__(self, mystars, savedstars):
		self.stars = mystars
		self.savedstars = savedstars

	def add_stars(self):
		''' Add new stars '''

		addables = [s for s in self.stars if s.name in { # star object if (valid) star not already saved
			s.name for s in self.stars if all([s.name,s.html_url]) # valid stars (name & url set)
		} - {
			p[0] for p in self.savedstars.values_list('name') # already saved stars
		}] # in valid stars but not in saved stars

		# Now we save the new ones
		for s in addables:
			Project(
                name=s.name,
                full_name=s.full_name or 'N/A',
                description=s.description or 'N/A',
                url=s.html_url,
                initial_stars=s.stargazers_count,
                current_stars=s.stargazers_count,
                language=Language.objects.get_or_create(name=s.language or 'N/A')[0]
            ).save()
			sleep(0.1) # treat the server nice

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

def get_ghh():
	''' get and store the auth handle in the cache for an hour '''
	ghh = pickle.loads(cache.get('ghh') or pickle.dumps(False))
	if not ghh:
		ghh = Github(settings.GH_USERNAME, settings.GH_PASSWORD).get_user(settings.GH_USERNAME)
		cache.set('ghh', pickle.dumps(ghh), 60*60)
	return ghh
