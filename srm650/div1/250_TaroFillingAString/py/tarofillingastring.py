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

        # Convert 1-indexed list of positions to 0-indexed
        position = map(lambda x: x - 1, position)

        # Sort the given string according to the given positions
        pos, value = zip(*(map(lambda x: (x[0], x[1]),
                               sorted(zip(position, value)))))

        # Reduce the length of the blank spots
        # Multiples of 3 can be reduced to 1, ex:
        # A___B (1, 5) can be reduced to A_B (1, 3)
        # Multiples of 2 can be reduced to 2, ex:
        # A____B (1, 6) can be reduced to A__B (1, 4)
        reduced_pos = list()
        for (start, end) in zip(*(islice((0,) + pos, n, None) for n in range(2))):
            if (end - start) < 2:
                interval = end - start
            elif (end - start) % 2 == 0:
                interval = 2
            # (end - start) % 2 == 1
            else:
                interval = 3
            reduced_pos.append((reduced_pos[-1] if reduced_pos else 0) + interval)

        S = range(reduced_pos[-1] + 1)
        blank_spots = set(S) - set(reduced_pos)

        for i, c in zip(reduced_pos, value):
            S[i] = c

        strings = product('AB', repeat=len(blank_spots))

        f = partial(helper, S, blank_spots, ugliness)
        # map tries to build a list out of the iterable, which is
        # terrible if the iterable is long (which it can be).
        # imap doesn't build the list in memory
        for r in pool.imap_unordered(f, strings, chunksize=1000):
            pass

        print time.time() - t0
        ugliness = dict(ugliness)
        return ugliness[min(ugliness)]


def main():
    t = TaroFillingAStringDiv1()
    # 2
    print t.getNumber(3, (1, 3), "AB")
    # 1
    print t.getNumber(4, (2, 1, 3, 4), "ABBA")
    # 1
    print t.getNumber(25, (23, 4, 8, 1, 24, 9, 16, 17, 6, 2, 25, 15, 14, 7, 13), "ABBBBABABBAAABA")
    # 43068480
    print t.getNumber(305,
            (183, 115, 250, 1, 188, 193, 163, 221, 144, 191, 92, 192, 58, 215, 157, 187, 227, 177, 206, 15, 272, 232, 49, 11, 178, 59, 189, 246),
            "ABAABBABBAABABBBBAAAABBABBBA")


if __name__ == '__main__':
    main()
