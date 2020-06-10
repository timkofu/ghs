
from time import sleep

from django.db.transaction import atomic

from celery import shared_task

from .models import Project, Language



@shared_task
@atomic
def mega_update(stars, savedstars, expected_exceptions, first_run=False):

	def add_stars():
		''' Add new stars '''

		addables = [s for s in stars if s.name in { # star object if (valid) star not already saved
			s.name for s in stars if all([s.name,s.html_url]) # valid stars (name & url set)
		} - {
			p[0] for p in savedstars.values_list('name') # already saved stars
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
	
	def update_metadata():
		''' Update starcount and descriptions '''
		for star in stars:
		    try:
		        saved_star = savedstars.get(full_name=star.full_name)
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
	
	def fallen():
		''' Delete unstared projects (fallen stars) '''
		current_stars = {x.full_name for x in stars}
		stored_stars = {x.full_name for x in savedstars}
		for fs in stored_stars - current_stars:
		    savedstars.get(full_name=fs).delete()

	# Here we go
	add_stars()
	if first_run: return # we are running the initialize_stars admin command, and we're done
	update_metadata();fallen()
