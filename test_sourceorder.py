#
# Copyright (C) 2014 pytest-sourceorder contributors. See COPYING for license
#

"""Test the ordering of tests

IPA integration tests, marked with `@ordered`, require tests to be run
in a specific order:
- Base classes first
- Within a class, test methods are ordered according to source line
"""

import functools

import pytest
from pytest_sourceorder import ordered

@pytest.fixture(scope='class')
def log():
    return [1]


def decorator(test_method):
    @functools.wraps(test_method)
    def wrapper(instance, *args, **kwargs):
        test_method(instance, *args, **kwargs)
    return wrapper


@ordered
class TestBase(object):
    def test_d_first(self, log):
        assert log == [1]
        log.append(2)


class TestChild(TestBase):
    def test_b_third(self, log):
        assert log == [1, 2, 3]
        log.append(4)

    @pytest.mark.parametrize('number', (5, 6, 7))
    def test_b_parametrized(self, log, number):
        assert log[-1] == number - 1
        log.append(number)

    def test_a_fourth(self, log):
        assert log == [1, 2, 3, 4, 5, 6, 7]
        log.append(8)

    @decorator
    def test_decorated(self, log):
        assert log == [1, 2, 3, 4, 5, 6, 7, 8]
        log.append(9)


def test_c_second(self, log):
    assert log == [1, 2]
    log.append(3)
TestBase.test_c_second = test_c_second
del test_c_second


@ordered
class TestUnrelated(object):
    def test_a(self):
        pass

    def test_b(self):
        pass

    def test_nose_generator(self):
        for i in range(2):
            yield (lambda x: i, i)

def test_unrelated():
    pass
