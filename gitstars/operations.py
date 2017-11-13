
class Ops:

	def __init__(self, mystars, savedstars):
		self.mystars = mystars
		self.savedstars = savedstars


	def add_stars(self, models, expected_exceptions):
		''' Add new stars '''
		for star in self.mystars:
			
			# Must have a name, full name and html url
			if not all([star.name,star.html_url]):continue

			try:
				models['project'](
	                name=star.name,
	                full_name=star.full_name or 'N/A',
	                description=star.description or 'N/A',
	                url=star.html_url,
	                initial_stars=star.stargazers_count,
	                current_stars=star.stargazers_count,
	                language=models['language'].objects.get_or_create(name=star.language or 'N/A')[0]
	            ).save()
			except expected_exceptions:
			    pass


	def fallen(self):
		''' Delete unstared projects '''
		current_stars = {x.full_name for x in self.mystars}
		stored_stars = {x.full_name for x in self.savedstars}
		fallen_stars = stored_stars.difference(current_stars)
		for fs in fallen_stars:
		    self.savedstars.get(full_name=fs).delete()


	def update_metadata(self, expected_exceptions):
		''' Update starcount and descriptions '''
		for star in self.mystars:
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
