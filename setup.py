from setuptools import setup

# Use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))


# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='thesmuggler',
    version='1.0.0',

    py_modules=['thesmuggler'],
    long_description=long_description,
    keywords='import modules packages files',
    license='MIT',

    author='Faraz Yashar',
    author_email='faraz.yashar@gmail.com',
    url='https://github.com/fny/thesmuggler',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ]
)
