from calc import Calculadora
import pytest


@pytest.fixture
def instance():
    return Calculadora()


def test_sum(instance):
    instance.primeiro = 1
    instance.segundo = 2
    assert instance.sum() == 3


def test_div(instance):
    instance.primeiro = 3
    instance.segundo = 2
    assert instance.div() == 1.5


# def test_div_zero(instance):
#     assert instance.div(3, 0) == 1.5

