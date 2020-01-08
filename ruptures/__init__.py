u"""
Offline change point detection for Python
====================================================================================================
"""

from __future__ import absolute_import
from .exceptions import NotEnoughPoints
from .datasets import pw_constant, pw_normal, pw_linear, pw_wavy
from .detection import (Binseg, BinsegHistory, BottomUp, Dynp, Omp, OmpK, Pelt, Window,
                        GreedyAR, GreedyLinear)
from .show import display
