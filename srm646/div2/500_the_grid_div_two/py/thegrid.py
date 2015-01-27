#!/usr/bin/env python


class TheGrid(object):
    def __init__(self):
        pass

    def find(self, blocked_x, blocked_y, seconds):
        def in_bounds(coords):
            return (coords[0] >= min_x and (min_y <= coords[1] <= max_y))

        X = 0
        Y = 1
        NORTH = (0, 1)
        SOUTH = (0, -1)
        WEST = (-1, 0)
        EAST = (1, 0)

        move_queue = list()
        visited = dict()
        blocked = zip(blocked_x, blocked_y)

        # shrink the board as much as possible by limiting how
        # far we can move on the -y, y, and x axes.
        min_x = (min(blocked, key=lambda pair: pair[X])[X] - 1) if blocked else -1
        min_x = min_x if min_x < 0 else -1

        max_y = (max(blocked, key=lambda pair: pair[Y])[Y] + 1) if blocked else 1
        max_y = max_y if max_y > 0 else 1
        min_y = (min(blocked, key=lambda pair: pair[Y])[Y] - 1) if blocked else -1
        min_y = min_y if min_y < 0 else -1

        # origin
        origin = (0, 0)
        move_queue.append([origin])
        visited.update({origin: origin[0]})

        for t in range(0, seconds):
            move_set = move_queue.pop()
            next_moves = list()
            for move in move_set:
                for direction in [NORTH, SOUTH, EAST, WEST]:
                    next_move = tuple([sum(x) for x in zip(move, direction)])
                    if next_move not in blocked and \
                       next_move not in visited.keys() and \
                       in_bounds(next_move):
                        visited.update({next_move: next_move[0]})
                        next_moves.append(next_move)
            move_queue.append(next_moves)

        return max(visited.values())


if __name__ == '__main__':
    grid = TheGrid()

    from timer import Timer
    with Timer() as t:
        print grid.find((1, 1, 1, 1), (-2, -1, 0, 1), 4)
    print t.interval

    with Timer() as t:
        print grid.find((-1, 0, 0, 1), (0, -1, 1, 0), 9)
    print t.interval

    with Timer() as t:
        print grid.find((1, 0, 0, -1, -1, -2, -2, -3, -3, -4, -4), (0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5), 47)
    print t.interval

    with Timer() as t:
        print grid.find((), (), 1000)
    print t.interval
