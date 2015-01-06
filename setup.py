# -*- coding: utf-8 -*-


from setuptools import setup
import brew_tools
NAME = 'brew_tools'

# README.rst dynamically generated:
with open('README.rst', 'w') as f:
    f.write(brew_tools.__doc__)

def read(file):
    with open(file, 'r') as f:
        return f.read().strip()

setup(
    name=NAME,
    version=read('VERSION'),
    description='Misc homebrew-related python modules/scripts',
    long_description=read('README.rst'),
    author='Mike Burr',
    author_email='mburr@unintuitive.org',
    url='https://github.com/stnbu/{0}'.format(NAME),
    download_url='https://github.com/stnbu/{0}/archive/master.zip'.format(NAME),
    provides=[NAME],
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
    ],
    packages=[NAME],
    keywords=[],
    entry_points={
        'console_scripts': [
            'brew_manage_glinks = {0}.run:run'.format(NAME),
            'manage_brew_glinks = {0}.run:run'.format(NAME),
        ]},
)
