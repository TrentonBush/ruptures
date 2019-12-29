from __future__ import absolute_import
from setuptools import setup, find_packages

setup(
    name=u'ruptures27',
    version=u'1.0.1',
    packages=find_packages(exclude=[u'docs', u'tests*', u'images']),
    install_requires=[u'numpy', u'scipy', u'backports.functools_lru_cache'],
    extras_require={
        u'display': [u'matplotlib']
    },
    python_requires=u'>=2.7',
    # url='ctruong.perso.math.cnrs.fr/ruptures',
    license=u'BSD License',
    author=u'Charles Truong, Laurent Oudre, Nicolas Vayatis',
    author_email=u'truong@cmla.ens-cachan.fr',
    description=u'Change point detection for signals, in Python',
    long_description=u"""\
Offline change point detection for Python. This version has been machine ported (with 3to2) to python 2.7. A backports.functools_lru_cache dependency was added for lru_cache functionality (needed in binseg detector).
-------------------------------------

__ruptures__ is a Python library for offline change point detection. This package provides methods for the analysis and segmentation of non-stationary signals. Implemented algorithms include exact and approximate detection for various parametric and non-parametric models. __ruptures__ focuses on ease of use by providing a well-documented and consistent interface. In addition, thanks to its modular structure, different algorithms and models can be connected and extended within this package.


An extensive documentation is available ctruong.perso.math.cnrs.fr/ruptures.
"""
)
