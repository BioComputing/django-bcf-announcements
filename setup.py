import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-bcf-announcements',
    version='0.1',
    packages=['bcf-announcements'],
    include_package_data=True,
    install_requires=['djangorestframework<=2.4'],
    license='BSD License',  # example license
    description='A django app for site-wide and user-targetted announcements.',
    long_description=README,
    url='https://github.com/nickeddy',
    author='Nicholas Eddy',
    author_email='eddy.nicholas@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
