u"""Factory function for Cost classes."""

from __future__ import absolute_import
from ruptures.base import BaseCost


def cost_factory(model, *args, **kwargs):
    for cls in BaseCost.__subclasses__():
        if cls.model == model:
            return cls(*args, **kwargs)
    raise ValueError(u"Not such model: {}".format(model))
