from distutils.core import setup
setup(
  name = 'gitstars',
  packages = ['gitstars'],
  version = '1.0.2',
  description = 'A Django app to help you manage your starred GitHub projects.',
  author = 'Timothy Makobu',
  author_email = 'timkofu@gmail.com',
  url = 'https://github.com/timkofu/gitstars',
  download_url = 'https://github.com/timkofu/gitstars/archive/1.0.2.tar.gz',
  keywords = ['python', 'django', 'github'],
  install_requires = [
    'django',
    'pygithub'
  ],
  packages = [
    'gitstars',
    'gitstars.migrations',
  ],
  classifiers = [],
)
