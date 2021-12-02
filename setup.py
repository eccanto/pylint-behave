"""
Setup module for Pylint plugin for Behave.
"""
from setuptools import setup, find_packages


with open('README.md', 'r', encoding='utf8') as readme:
    long_description = readme.read()


setup(
    name='pylint-behave',
    version='1.0.0',
    url='https://github.com/eccanto/pylint-behave',
    author='Erik Ccanto',
    author_email='ccanto.erik@gmail.com',
    description='A Pylint plugin to help Pylint understand the Behave projects',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='GPLv2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'behave>=1.2.5',
        'pylint>=2.0',
        'pylint-plugin-utils>=0.5',
    ],
    python_requires='>=3.6.2',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: Unix',
        'Topic :: Software Development :: Quality Assurance',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Framework :: Behave :: 1.2.5',
        'Framework :: Behave :: 1.2.6',
    ],
    keywords=['pylint', 'behave', 'plugin'],
    zip_safe=False,
)
