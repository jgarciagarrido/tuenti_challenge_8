#!/usr/bin/env python
# -*- coding: utf-8 -*-

MOVES = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
         (1, -2), (1, 2), (2, -1), (2, 1)]
SUPERMOVES = map(lambda pos: map(lambda x: x*2, pos), MOVES)


def position(grid, character, rows, columns):
    for i in xrange(rows):
        for j in xrange(columns):
            if grid[i][j] == character:
                return {'x': j, 'y': i}
    return None


def in_range(x, n):
    return x >= 0 and x < n


def is_in_grid(pos, n, m):
    return in_range(pos['y'], n) and in_range(pos['x'], m)


def init_visited_grid(n, m):
    visited = []
    for i in xrange(n):
        row = []
        for j in xrange(m):
            row.append(False)
        visited.append(row)
    return visited


def min_jumps_to_target(grid, n, m, origin, target):
    origin['dist'] = 0
    pos_queue = [origin]
    visited = init_visited_grid(n, m)
    visited[origin['y']][origin['x']] = True
    while len(pos_queue) > 0:
        current = pos_queue.pop(0)
        x = current['x']
        y = current['y']
        dist = current['dist']
        if(x == target['x'] and y == target['y']):
            return dist
        moves = MOVES
        if grid[y][x] == '*':
            moves = SUPERMOVES
        for move in moves:
            new_pos = {
                'y': y + move[0],
                'x': x + move[1]
            }
            if (is_in_grid(new_pos, n, m) and
               not visited[new_pos['y']][new_pos['x']]):
                visited[new_pos['y']][new_pos['x']] = True
                if grid[new_pos['y']][new_pos['x']] != '#':
                    new_pos['dist'] = dist + 1
                    pos_queue.append(new_pos)
    return "IMPOSSIBLE"


def min_jumps_to_rescue(grid, n, m):
    position_knight = position(grid, 'S', n, m)
    position_princess = position(grid, 'P', n, m)
    position_exit = position(grid, 'D', n, m)
    dist_to_princess = min_jumps_to_target(
        grid, n, m, position_knight, position_princess)
    dist_to_exit = min_jumps_to_target(
        grid, n, m, position_princess, position_exit)
    if dist_to_princess == 'IMPOSSIBLE' or dist_to_exit == 'IMPOSSIBLE':
        return 'IMPOSSIBLE'
    return dist_to_princess + dist_to_exit


if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(1, t + 1):
        n, m = [int(s) for s in raw_input().split(" ")]
        grid = []
        for j in xrange(n):
            grid.append(raw_input())

        print "Case #{}: {}".format(i, min_jumps_to_rescue(grid, n, m))
