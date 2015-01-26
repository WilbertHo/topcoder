#!/usr/bin/env python

from nose.tools import eq_

def test_find():
    eq_(find((1, 1, 1, 1), (-2, -1, 0, 1), 4), 2)
    eq_(find((-1, 0, 0, 1), (0, -1, 1, 0), 9), 0)
    eq_(find((), (), 1000), 1000)
    eq_(find((1, 0, 0, -1, -1, -2, -2, -3, -3, -4, -4), (0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5), 47), 31)
