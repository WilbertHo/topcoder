from collections import defaultdict
from functools import partial
from itertools import islice, product
from multiprocessing import Manager, Pool
import time


def helper(S, blank_spots, ugliness, string):
    for i, c in zip(blank_spots, string):
        S[i] = c

    ugly_count = 0
    # Compare every 2 characters in the string
    for a, b in zip(*(islice(S, n, None) for n in range(2))):
        if a == b:
            ugly_count += 1

    ugliness[ugly_count] = ugliness.get(ugly_count, 0) + 1


class TaroFillingAStringDiv1(object):
    def getNumber(self, N, position, value):
        t0 = time.time()
        manager = Manager()
        pool = Pool()
        ugliness = manager.dict()
        S = range(N)
        position = map(lambda x: x - 1, position)
        blank_spots = set(S) - set(position)

        for i, c in zip(position, value):
            S[i] = c

        strings = product('AB', repeat=len(blank_spots))

        f = partial(helper, S, blank_spots, ugliness)
        for r in pool.imap_unordered(f, strings, chunksize=1000):
            pass

        print time.time() - t0
        ugliness = dict(ugliness)
        return ugliness[min(ugliness)]


def main():
    t = TaroFillingAStringDiv1()
    print t.getNumber(3, (1, 3), "AB")
    print t.getNumber(4, (2, 1, 3, 4), "ABBA")
    print t.getNumber(25, (23, 4, 8, 1, 24, 9, 16, 17, 6, 2, 25, 15, 14, 7, 13), "ABBBBABABBAAABA")
    print t.getNumber(305,
            (183, 115, 250, 1, 188, 193, 163, 221, 144, 191, 92, 192, 58, 215, 157, 187, 227, 177, 206, 15, 272, 232, 49, 11, 178, 59, 189, 246),
            "ABAABBABBAABABBBBAAAABBABBBA")


if __name__ == '__main__':
    main()
