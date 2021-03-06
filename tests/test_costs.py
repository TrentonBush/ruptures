from __future__ import with_statement
from __future__ import absolute_import
import numpy as np
import pytest

from ruptures.costs import CostAR, CostL1, CostL2, CostLinear, CostNormal, CostRbf, cost_factory
from ruptures.datasets import pw_constant
from ruptures.exceptions import NotEnoughPoints


@pytest.fixture(scope=u"module")
def signal_bkps_1D():
    signal, bkps = pw_constant(n_features=1)
    return signal, bkps


@pytest.fixture(scope=u"module")
def signal_bkps_1D_noisy():
    signal, bkps = pw_constant(n_features=1, noise_std=1)
    return signal, bkps


@pytest.fixture(scope=u"module")
def signal_bkps_5D():
    signal, bkps = pw_constant(n_features=5)
    return signal, bkps


@pytest.fixture(scope=u"module")
def signal_bkps_5D_noisy():
    signal, bkps = pw_constant(n_features=5, noise_std=1)
    return signal, bkps


@pytest.mark.parametrize(u"cost", [CostAR, CostL1, CostL2, CostNormal, CostRbf])
def test_costs_1D(signal_bkps_1D, cost):
    signal, bkps = signal_bkps_1D
    cost.fit(signal)
    cost.fit(signal.flatten())
    cost.error(0, 100)
    cost.error(100, signal.shape[0])
    cost.error(10, 50)
    cost.sum_of_costs(bkps)
    with pytest.raises(NotEnoughPoints):
        cost.error(1, 2)


@pytest.mark.parametrize(u"cost", [CostAR, CostL1, CostL2, CostNormal, CostRbf])
def test_costs_1D_noisy(signal_bkps_1D_noisy, cost):
    signal, bkps = signal_bkps_1D_noisy
    cost.fit(signal)
    cost.fit(signal.flatten())
    cost.error(0, 100)
    cost.error(100, signal.shape[0])
    cost.error(10, 50)
    cost.sum_of_costs(bkps)
    with pytest.raises(NotEnoughPoints):
        cost.error(1, 2)


@pytest.mark.parametrize(u"cost", [CostLinear, CostL1, CostL2, CostNormal, CostRbf])
def test_costs_5D(signal_bkps_5D, cost):
    signal, bkps = signal_bkps_5D
    cost.fit(signal)
    cost.error(0, 100)
    cost.error(100, signal.shape[0])
    cost.error(10, 50)
    cost.sum_of_costs(bkps)
    with pytest.raises(NotEnoughPoints):
        cost.error(1, 2)


@pytest.mark.parametrize(u"cost", [CostLinear, CostL1, CostL2, CostNormal, CostRbf])
def test_costs_5D_noisy(signal_bkps_5D_noisy, cost):
    signal, bkps = signal_bkps_5D_noisy
    cost.fit(signal)
    cost.error(0, 100)
    cost.error(100, signal.shape[0])
    cost.error(10, 50)
    cost.sum_of_costs(bkps)
    with pytest.raises(NotEnoughPoints):
        cost.error(1, 2)


@pytest.mark.parametrize(u"cost_name", [u"ar", u"l1", u"l2", u"normal", u"rbf"])
def test_costs_1D(signal_bkps_1D, cost_name):
    signal, bkps = signal_bkps_1D
    cost = cost_factory(cost_name)
    cost.fit(signal)
    cost.fit(signal.flatten())
    cost.error(0, 100)
    cost.error(100, signal.shape[0])
    cost.error(10, 50)
    cost.sum_of_costs(bkps)
    with pytest.raises(NotEnoughPoints):
        cost.error(1, 2)


@pytest.mark.parametrize(u"cost_name", [u"ar", u"l1", u"l2", u"normal", u"rbf"])
def test_costs_1D_noisy(signal_bkps_1D_noisy, cost_name):
    signal, bkps = signal_bkps_1D_noisy
    cost = cost_factory(cost_name)
    cost.fit(signal)
    cost.fit(signal.flatten())
    cost.error(0, 100)
    cost.error(100, signal.shape[0])
    cost.error(10, 50)
    cost.sum_of_costs(bkps)
    with pytest.raises(NotEnoughPoints):
        cost.error(1, 2)


@pytest.mark.parametrize(u"cost_name", [u"linear", u"l1", u"l2", u"normal", u"rbf"])
def test_costs_5D(signal_bkps_5D, cost_name):
    signal, bkps = signal_bkps_5D
    cost = cost_factory(cost_name)
    cost.fit(signal)
    cost.error(0, 100)
    cost.error(100, signal.shape[0])
    cost.error(10, 50)
    cost.sum_of_costs(bkps)
    with pytest.raises(NotEnoughPoints):
        cost.error(1, 2)


@pytest.mark.parametrize(u"cost_name", [u"linear", u"l1", u"l2", u"normal", u"rbf"])
def test_costs_5D_noisy(signal_bkps_5D_noisy, cost_name):
    signal, bkps = signal_bkps_5D_noisy
    cost = cost_factory(cost_name)
    cost.fit(signal)
    cost.error(0, 100)
    cost.error(100, signal.shape[0])
    cost.error(10, 50)
    cost.sum_of_costs(bkps)
    with pytest.raises(NotEnoughPoints):
        cost.error(1, 2)


def test_factory_exception():
    with pytest.raises(ValueError):
        cost_factory(u"bkd;s")
