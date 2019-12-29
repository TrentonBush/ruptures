u"""Base class for change point detection estimators."""
from __future__ import absolute_import
import abc
from ruptures.utils import pairwise


class BaseEstimator(object):

    __metaclass__ = abc.ABCMeta
    u"""Base class for all change point detection estimators.

    Notes
    -----
    All estimators should specify all the parameters that can be set
    at the class level in their ``__init__`` as explicit keyword
    arguments (no ``*args`` or ``**kwargs``).
    """

    @abc.abstractmethod
    def fit(self, *args, **kwargs):
        u""" To call the segmentation algorithm"""
        pass

    @abc.abstractmethod
    def predict(self, *args, **kwargs):
        u""" To call the segmentation algorithm"""
        pass

    @abc.abstractmethod
    def fit_predict(self, *args, **kwargs):
        u""" To call the segmentation algorithm"""
        pass


class BaseCost(object):

    __metaclass__ = abc.ABCMeta
    u"""Base class for all segment cost classes.

    Notes
    -----
    All classes should specify all the parameters that can be set
    at the class level in their ``__init__`` as explicit keyword
    arguments (no ``*args`` or ``**kwargs``).
    """

    @abc.abstractmethod
    def fit(self, *args, **kwargs):
        u"""Set the parameters of the cost function, for instance the Gram matrix, etc."""
        pass

    @abc.abstractmethod
    def error(self, start, end):
        u"""Returns the cost on segment [start:end]."""
        pass

    def sum_of_costs(self, bkps):
        u"""Returns the sum of segments cost for the given segmentation.

        Args:
            bkps (list): list of change points. By convention, bkps[-1]==n_samples.

        Returns:
            float: sum of costs
        """
        soc = sum(self.error(start, end)
                  for start, end in pairwise([0] + bkps))
        return soc

    @property
    @abc.abstractmethod
    def model(self):
        pass
