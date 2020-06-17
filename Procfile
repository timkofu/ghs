release: python manage.py migrate
web: uvicorn githubstars.asgi:application --host=0.0.0.0 --port=$PORT
