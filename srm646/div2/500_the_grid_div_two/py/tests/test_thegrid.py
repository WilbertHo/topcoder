#!/usr/bin/env python

from nose.tools import eq_

from thegrid import TheGrid


def test_find():
    grid = TheGrid()

    eq_(grid.find((1, 1, 1, 1), (-2, -1, 0, 1), 4), 2)
    eq_(grid.find((1, 0, 0, -1, -1, -2, -2, -3, -3, -4, -4), (0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5), 47), 31)


def test_find_big():
    grid = TheGrid()

    eq_(grid.find((), (), 1000), 1000)


def test_find_small():
    grid = TheGrid()

    eq_(grid.find((-1, 0, 0, 1), (0, -1, 1, 0), 9), 0)
