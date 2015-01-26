#
# Copyright (C) 2014 pytest-sourceorder contributors. See COPYING for license
#

"""Pytest plugin for running tests in source order

Adds support for the @pytest.mark.source_order decorator which,
when applied to a class, runs the test methods in source order.

See test_ordering for an example.
"""

import unittest

import pytest


def ordered(cls):
    """Decorator that marks a test class as ordered

    Methods within the marked class will be executed in definition order
    (or more strictly, in ordered by the line number where they're defined).

    Subclasses of unittest.TestCase can not be ordered.

    Generator methods will not be ordered by this plugin.
    """
    cls._order_plugin__ordered = True
    assert not isinstance(cls, unittest.TestCase), (
        "A unittest.TestCase may not be ordered.")
    cls = pytest.mark.source_order(cls)
    return cls


def decorate_items(items):
    node_indexes = {}
    for index, item in enumerate(items):
        try:
            func = item.function
        except AttributeError:
            yield (index, ), item
            continue

        key = (index, )
        for node in reversed(item.listchain()):
            # Find the corresponding class
            if isinstance(node, pytest.Class):
                cls = node.cls
            else:
                continue
            if getattr(cls, '_order_plugin__ordered', False):
                node_index = node_indexes.setdefault(node, index)
                # Find first occurence of the method in class hierarchy
                for i, parent_class in enumerate(reversed(cls.mro())):
                    if getattr(parent_class, '_order_plugin__ordered', False):
                        method = getattr(parent_class, func.__name__, None)
                        if method:
                            # Sort methods as tuples  (position of the class
                            # in the inheritance chain, position of the method
                            # within that class)
                            key = (node_index, 0,
                                   i, method.__code__.co_firstlineno, node)
                            break
                else:
                    # Weird case fallback
                    # Method name not in any of the classes in MRO, run it last
                    key = node_index, 1, func.__code__.co_firstlineno, node
                break
        yield key, item


def pytest_collection_modifyitems(session, config, items):
    items[:] = [item for i, item in sorted(decorate_items(items))]
