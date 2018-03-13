
import pickle

from django.conf import settings
from django.core.cache import cache

from github import Github



def get_ghh():
	''' get and store the auth handle in the cache for an hour '''
	ghh = pickle.loads(cache.get('ghh') or pickle.dumps(False))
	if not ghh:
		ghh = Github(settings.GH_USERNAME, settings.GH_PASSWORD).get_user(settings.GH_USERNAME)
		cache.set('ghh', pickle.dumps(ghh), 60*60)
	return ghh
