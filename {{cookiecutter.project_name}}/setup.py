#!/usr/bin/env python

import re

from codecs import open

from setuptools import setup

packages = [
    '{{cookiecutter.project_name}}',
]

version = ''
with open('{{cookiecutter.project_name}}/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='{{cookiecutter.project_name}}',
    version=version,
    description='{{cookiecutter.description}}',
    long_description=readme,
    author="{{cookiecutter.author_name}}",
    author_email='{{cookiecutter.author_email}}',
    url='https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}',
    license='{{cookiecutter.license}}',
    classifiers=(
        'Development Status :: 2 - Pre-alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7'
    ),
    entry_points={
        'console_scripts': [
            '{{cookiecutter.project_name}} = {{cookiecutter.project_name}}.cli:run',
        ],
    },
    packages=['{{cookiecutter.project_name}}'],
    test_suite='test',
    install_requires=['click', 'flake8'],
    tests_require=['pbr==1.6', 'mock'],
)
