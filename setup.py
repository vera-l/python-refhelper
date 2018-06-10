#! /usr/bin/python
# coding: utf8

from setuptools import setup

setup(
    name='refhelper',
    version='0.1',
    description='Python refactoring helper',
    long_description='A tool for easy refactoring with some tasks',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='profiler',
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
