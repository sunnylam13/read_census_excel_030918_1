try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'A program that goes through census data spreadsheets row by row and tallies up the population numbers.  It also calculates the statistics for each county.',
	'author': 'Sunny Lam',
	'url': 'https://github.com/sunnylam13/read_census_excel_030918_1',
	'download_url': 'https://github.com/sunnylam13/read_census_excel_030918_1',
	'author_email': 'sunny.lam@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['openpyxl'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)