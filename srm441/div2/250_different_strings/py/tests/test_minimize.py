#!/usr/bin/env python

from differentstrings import DifferentStrings

from nose.tools import eq_


def test_minimize():
    df = DifferentStrings()

    eq_(df.minimize('koder', 'topcoder'), 1)
    eq_(df.minimize('hello', 'xello'), 1)
    eq_(df.minimize('abc', 'topabcoder'), 0)
    eq_(df.minimize('adaabc', 'aababbc'), 2)
    eq_(df.minimize('giorgi', 'igroig'), 6)
    eq_(df.minimize('a', 'b'), 1)
    eq_(df.minimize('', ''), 0)
    eq_(df.minimize('', 'a'), 0)
    eq_(df.minimize('', 'aba'), 0)
    eq_(df.minimize('', 'abac'), 0)
