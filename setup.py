# Automatically created by: shub deploy

from setuptools import setup, find_packages

setup(
    name         = 'project',
    version      = '2.0',
    packages     = find_packages(),
    scripts      = ['run.py'],
    package_data = {
        'Automotive_web_scraping': ['configurations/*.json', 'templates/*']
    },
    entry_points = {'scrapy': ['settings = Automotive_web_scraping.settings']},
    include_package_data=True,
)