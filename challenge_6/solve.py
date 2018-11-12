#!/usr/bin/env python
# -*- coding: utf-8 -*-


def create_intervals(notes):
    return [(note[0]/note[2], (note[0]+note[1])/note[2], note[3])
            for note in notes]


def find_max_score_interval(intervals):
    return max(intervals, key=lambda x: x[2])


def reduce_combos(intervals):
    return [[x[0], x[1], x[2]*intervals.count(x)]
            for x in list(set(intervals))]


def is_common(x, left, right):
    return (x[1] >= left and x[1] <= right) or (x[0] <= right and x[0] >= left)


def max_possible_score(intervals):
    if len(intervals) == 0:
        return 0
    if len(intervals) == 1:
        return intervals[0][2]
    max_interval = find_max_score_interval(intervals)
    # print "max: {}".format(max_interval)
    max_score = max_interval[2]
    left = max_interval[0]
    right = max_interval[1]
    interval_same = [x for x in intervals if is_common(x, left, right)]
    interval_same.remove(max_interval)
    # print "same: {}".format(interval_same)
    while len(interval_same) > 0:
        max_interval_same = max_possible_score(interval_same)
        if max_interval_same > max_score:
            max_score = max_interval_same
            left = min([x[0] for x in interval_same])
            right = max([x[0] for x in interval_same])
            new_interval_same = [x for x in intervals if is_common(x, left, right)]
            for interval in interval_same:
                new_interval_same.remove(interval)
            interval_same = new_interval_same
            # print "same: {}".format(interval_same)
        else:
            break

    interval_left = [x for x in intervals if x[1] < left]
    # print "left: {}".format(interval_left)
    interval_right = [x for x in intervals if x[0] > right]
    # print "right: {}".format(interval_right)
    result = (
        max_possible_score(interval_left) +
        max_possible_score(interval_right) +
        max_score)
    # print "Result: {}".format(result)
    return result


if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(1, t + 1):
        lines = int(raw_input())
        notes = []
        for j in xrange(lines):
            note = [int(s) for s in raw_input().split(" ")]
            notes.append(note)
        intervals = create_intervals(notes)
        intervals =sorted(reduce_combos(intervals))
        # for interval in intervals:
        #      print interval
        print "Case #{}: {}".format(i, max_possible_score(intervals))
