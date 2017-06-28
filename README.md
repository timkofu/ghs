# Gitstars

A Django app that stores your git stars in a database, where you can filter and
search, to make it easier for you to find what you starred.

![screen_shot](https://raw.githubusercontent.com/timkofu/timkofu.github.io/master/fls/gitstars_screen_shot.jpg)

Note: It wont save a project unless the following fields are populated:
* name
* full_name
* language
* description
* html_url
* stargazers_count

## Installation
`pip install gitstars`
Then in settings.py:
* Add `gitstars` to `INSTALLED_APPS`
* Set `GH_USERNAME` and `GH_PASSWORD` (github username and password)
* Run `python manage.py migrate`
* Run `python manage.py initialize_stars`

Enjoy ✨
