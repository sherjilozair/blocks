from codecs import open
from os import path
from setuptools import find_packages, setup

import blocks

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    while not f.readline().startswith('Blocks'):  # Skip the badges
        pass
    long_description = 'Blocks\n' + f.read().strip()

setup(
    name='blocks',
    version=blocks.__version__,
    description='Toolbox for building machine learning models with Theano',
    long_description=long_description,
    url='https://github.com/bartvm/blocks',
    author='University of Montreal',
    license='MIT',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='theano machine learning neural networks deep learning',
    packages=find_packages(exclude=['docs', 'tests']),
    install_requires=['numpy', 'scipy', 'theano', 'six'],
    extras_require={
        'test': ['nose', 'nose2'],
    },
)
