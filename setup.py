# to distribute:
# python setup.py register sdist upload

from setuptools import setup
import sys
import os

try:
    ## Remove 'MANIFEST' file to force
    ## distutils to recreate it.
    ## Only in "sdist" stage. Otherwise
    ## it makes life difficult to packagers.
    if sys.argv[1] == "sdist":
        os.unlink("MANIFEST")
except:
    pass

setup(
    name="pyclitool",
    version="1.0",
    scripts=['py'],
    author="Ron Reiter",
    author_email="ron.reiter@gmail.com",
    url="http://github.com/ronreiter/pyclitools",
    license="MIT",
    description="pyclitool is a command line utility that allow you to map/filter/reduce your input with a Python one liner, line by line.",
    long_description=open(os.path.join(os.path.dirname(__file__), "README.md")).read(),
)
