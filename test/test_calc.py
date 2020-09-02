from calc import Calculadora
import pytest


@pytest.fixture
def instance():
    return Calculadora()


def test_sum(instance):
    assert instance.sum(1, 2) == 3


def test_div(instance):
    assert instance.div(3, 2) == 1.5


# def test_div_zero(instance):
#     assert instance.div(3, 0) == 1.5

