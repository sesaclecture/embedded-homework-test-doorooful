#!/usr/bin/env python3
""" test """

from src.main import add


def test_add():
    """ test """
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
