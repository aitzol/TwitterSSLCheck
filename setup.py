from setuptools import setup, find_packages
import sys, os

version = 'Check new Twitter SSL support'

setup(name='TwitterSSLCheck',
      version=version,
      description="",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Aitzol Naberan',
      author_email='anaberan@codesyntax.com',
      url='http://www.codesyntax.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'tweepy',
      ],
      entry_points={
        'console_scripts': [
              'check_ssl = twittersslcheck.test_ssl:main',
        ]
        },
      )
