import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='geopal-python-client',
    version='0.1',
    packages=['geopal-client'],
    include_package_data=True,
    license='BSD License',  # example license
    description='A simple GeoPal python client.',
    long_description=README,
    url='https://github.com/geopal-solutions/geopal-api-samples/tree/master/samples/python',
    author='GeoPal',
    author_email='support@geopal-solutions.com',
    classifiers=[
        'Environment :: Server Environment',
        'Framework :: Framework Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)