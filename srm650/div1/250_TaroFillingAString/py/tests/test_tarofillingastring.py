from nose.tools import eq_
import tarofillingastring


def test_getnumber():
    t = tarofillingastring.TaroFillingAStringDiv1()
    eq_(t.getNumber(3, (1, 3), "AB"), 2)
    eq_(t.getNumber(4, (2, 1, 3, 4), "ABBA"), 1)
    eq_(t.getNumber(25,
                    (23, 4, 8, 1, 24, 9, 16, 17, 6, 2, 25, 15, 14, 7, 13),
                    "ABBBBABABBAAABA"), 1)
    eq_(t.getNumber(305,
                    (183, 115, 250, 1, 188, 193, 163, 221, 144, 191, 92, 192, 58, 215, 157, 187, 227, 177, 206, 15, 272, 232, 49, 11, 178, 59, 189, 246),
                    "ABAABBABBAABABBBBAAAABBABBBA"), 43068480)
