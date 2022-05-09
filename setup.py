
from setuptools import setup, find_packages
from alcampo.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='alcampo',
    version=VERSION,
    description='Alcampo reporter',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Damien de St Laurent',
    author_email='damien.desaintlaurent@wl.com',
    url='https://github.com/damiendsl/alcampo',
    license='unlicensed',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'alcampo': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        alcampo = alcampo.main:main
    """,
)
