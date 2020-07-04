import os
import subprocess

from setuptools import setup, find_packages, Command
from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip


pfile = Project(chdir=False).parsed_pipfile
requirements = convert_deps_to_pip(pfile['packages'], r=False)
test_requirements = convert_deps_to_pip(pfile['dev-packages'], r=False)


class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        subprocess.check_call(
            'rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info ./__pycache__',
            stderr=subprocess.STDOUT,
            stdout=subprocess.DEVNULL,
            shell=True
        )


setup(
    
    name="Githubstars",
    version="2.0",
    author="Timothy Makobu",
    description="Get insight into your stared projects",
    packages=find_packages(),  # This needs __init__.py in each package (folder)
    
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: POSIX",
        "Environment :: Web Environment"
    ],

    python_requires=">=3.8",
    install_requires=[requirements, test_requirements],
    
    cmdclass={
        'clean': CleanCommand,
    }

)
