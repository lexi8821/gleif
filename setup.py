from distutils.core import setup

setup(
    # Application name
    name="gleif",

    # Version number (initial):
    version = "0.4",

    # Application author details:
    author="Tomas Olexa",
    author_email = "tomas.olexa@hotmail.com",

    # Packages
    packages=['gleif'],

    # Include additional files into package
    include_package_data=True,

    # Details
    url = "http://pypi.python.org/pypi/gleif",

    # Licence
    licence="LICENCE.txt"

    # Short description
    description="GLEIF database API python interface.",

    # Long description
    long_description = open('README.txt').read(),

    # Dependent packages
    install_requires=[
        "requests",
    ],
)
