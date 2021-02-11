#! /usr/bin/python3

from setuptools import setup

from refhelper.version import version

setup(
    name='refhelper',
    version=version,
    description='Python refactoring helper',
    long_description='A tool for easy refactoring with some tasks',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='refactoring tool',
    url='http://iamvera.com',
    author='Vera Lobacheva',
    author_email='vera@iamvera.com',
    license='MIT',
    packages=['refhelper'],
    install_requires=[
        'jinja2',
    ],
    include_package_data=True,
    package_data={
        'refhelper': ['report.tpl']
    },
    zip_safe=False,
    scripts=['pyrefhelper'],
)
