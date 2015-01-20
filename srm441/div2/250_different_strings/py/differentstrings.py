#!/usr/bin/env python


class DifferentStrings(object):
    def minimize(self, shorter, longer):
        max_match = 0   # largest number of matching letters so far
        match_index = 0 # index where max_match starts

        for i in range(0, len(longer) - len(shorter) + 1):
            match_count = 0     # number of matching letters
            for j, letter in enumerate(shorter):
                # compare 'topcoder' to 'koder', 'opcoder' to 'koder', etc
                if letter == longer[i:][j]:
                    match_count += 1
            if match_count > max_match:
                # save the index where the largest number of matches are found
                max_match = match_count
                match_index = i

        # construct the best matching string we can find by filling in
        # letters from the beginning of the longer string until we
        # reach the match index, then add the shorter string, then
        # fill in any remaining letters from the longer string
        best_match = longer[:match_index] + \
                     shorter + \
                     longer[len(longer[:match_index]) + len(shorter):]

        # Count up the number of letters that differ from the longer string
        # by zipping the two and comparing the two tuple elements
        # ex ('c', 'k')
        return len(filter(lambda x: x[0] != x[1], zip(longer, best_match)))


def main():
    df = DifferentStrings()
    print df.minimize('koder', 'topcoder')
    print df.minimize('hello', 'xello')
    print df.minimize('a', 'b')
    print df.minimize('', '')


if __name__ == '__main__':
    main()
