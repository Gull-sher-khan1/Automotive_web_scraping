# Automatically created by: shub deploy

from setuptools import setup, find_packages

setup(
    name         = 'project',
    version      = '1.0',
    packages     = find_packages(),
    scripts      = ['run.py'],
    entry_points = {'scrapy': ['settings = Automotive_web_scraping.settings']},
)
from setuptools import setup, find_packages