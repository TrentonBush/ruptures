ur"""Draw a random partition."""

from __future__ import division
from __future__ import absolute_import
import numpy as np
from numpy.random import dirichlet


def draw_bkps(n_samples=100, n_bkps=3):
    u"""Draw a random partition with specified number of samples and specified number of changes."""
    alpha = np.ones(n_bkps + 1) / (n_bkps + 1) * 2000
    bkps = np.cumsum(dirichlet(alpha) * n_samples).astype(int).tolist()
    bkps[-1] = n_samples
    return bkps
