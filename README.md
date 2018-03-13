# Gitstars

A Django app that stores your git stars in a database, where you can filter and
search, to make it easier for you to find what you starred.

![screen_shot](https://raw.githubusercontent.com/timkofu/timkofu.github.io/master/fls/gs.png)

## Installation

`pip install gitstars`

Django environment:

* Setup Celery
* In settings.py:
  * Add `gitstars` to `INSTALLED_APPS`
  * Set `GH_USERNAME` and `GH_PASSWORD` (github username and password)
  * Run `python manage.py migrate`
  * Run `python manage.py initialize_stars`

Enjoy ✨
