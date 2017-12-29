from distutils.core import setup
setup(
  name = 'gitstars',
  version = '1.2.3',
  description = 'A Django app to help you manage your starred GitHub projects.',
  author = 'Timothy Makobu',
  author_email = 'timkofu@gmail.com',
  url = 'https://github.com/timkofu/gitstars',
  download_url = 'https://github.com/timkofu/gitstars/archive/1.2.3.tar.gz',
  keywords = ['python', 'django', 'github'],
  install_requires = [
    'django',
    'pygithub'
  ],
  packages = [
    'gitstars',
    'gitstars.migrations',
    'gitstars.management.commands',
  ],
  classifiers = [],
)
