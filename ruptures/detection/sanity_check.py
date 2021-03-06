from __future__ import division
from __future__ import absolute_import
from math import ceil


def sanity_check(n_samples, n_bkps, jump, min_size):
    u"""Check if a partition if possible given the parameters.

    Args:
        n_samples (int): number of point in the signal
        n_bkps (int): number of breakpoints
        jump (int): the start index of each regime can only be a multiple of
            "jump" (and the end index = -1 modulo "jump").
        min_size (int): the minimum size of a segment.

    Returns:
        bool: True if there exists a potential configuration of
            breakpoints for the given parameters. False if it does not.
    """
    n_adm_bkps = n_samples // jump  # number of admissible breakpoints

    # Are there enough points for the given number of regimes?
    if n_bkps > n_adm_bkps:
        return False
    if n_bkps * ceil(min_size / jump) * jump + min_size > n_samples:
        return False
    return True
