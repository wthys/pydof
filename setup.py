import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pydof",
    version = "0.1a",
    author = "Wim Thys",
    author_email = "wim.thys@zardof.be",
    description = ("Bandwith monitor for Belgian ISP Telenet"),
    scripts = ["scripts/pydof-usage", "scripts/pydof-total"],
    license = "GPLv3",
    keywords = "telenet bandwith monitor",
    url = "http://www.zardof.be/python/pydof",
    packages=['pydof'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
	"Intended Audience :: Developers",
	"License :: OSI Approved :: GNU General Public License (GPL)",
	"Programming Language :: Python",
	"Topic :: Software Development :: Libraries :: Python Modules",
	"Topic :: Utilities"
    ],
)
